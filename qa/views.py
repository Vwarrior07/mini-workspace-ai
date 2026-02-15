import re
from django.shortcuts import render
from documents.models import Document
from .services import generate_answer
from runs.models import Run


def tokenize(text):
    """
    Clean and tokenize text into lowercase words,
    removing punctuation and noise.
    """
    return set(re.findall(r'\b\w+\b', text.lower()))


def ask_question(request):
    answer = None
    source_document = None
    excerpt = None

    if request.method == "POST":
        question = request.POST.get("question", "").strip()

        if not question:
            answer = "Please enter a valid question."
        else:
            documents = Document.objects.all()

            best_doc = None
            doc_max_score = 0

            question_words = tokenize(question)

            # ---------- Document Level Scoring ----------
            for doc in documents:
                content_words = tokenize(doc.content)
                score = len(question_words.intersection(content_words))

                if score > doc_max_score:
                    doc_max_score = score
                    best_doc = doc

            if best_doc and doc_max_score > 0:

                # ---------- Sentence-Based Chunking (Better for PDFs) ----------
                sentences = re.split(r'(?<=[.!?])\s+', best_doc.content)

                best_chunk = ""
                chunk_max_score = 0

                for sentence in sentences:
                    sentence_words = tokenize(sentence)
                    score = len(question_words.intersection(sentence_words))

                    if score > chunk_max_score:
                        chunk_max_score = score
                        best_chunk = sentence

                context = best_chunk if best_chunk else best_doc.content[:2000]

                answer = generate_answer(question, context)
                source_document = best_doc.name
                excerpt = context[:300]

            else:
                answer = "No relevant document found."

            # ---------- Save Run ----------
            Run.objects.create(
                question=question,
                answer=answer,
                source_document=source_document,
                excerpt=excerpt
            )

    return render(request, "qa/ask.html", {
        "answer": answer,
        "source_document": source_document,
        "excerpt": excerpt
    })
