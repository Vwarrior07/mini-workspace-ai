from django.shortcuts import render
from documents.models import Document
from .services import generate_answer
from runs.models import Run


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

            question_words = set(question.lower().split())

            for doc in documents:
                content_words = set(doc.content.lower().split())
                score = len(question_words.intersection(content_words))

                if score > doc_max_score:
                    doc_max_score = score
                    best_doc = doc

            if best_doc and doc_max_score > 0:

                paragraphs = best_doc.content.split("\n")

                best_paragraph = ""
                para_max_score = 0

                for para in paragraphs:
                    para_words = set(para.lower().split())
                    score = len(question_words.intersection(para_words))

                    if score > para_max_score:
                        para_max_score = score
                        best_paragraph = para

                # Use best matching paragraph
                context = best_paragraph if best_paragraph else best_doc.content[:2000]

                answer = generate_answer(question, context)
                source_document = best_doc.name
                excerpt = context[:300]

            else:
                answer = "No relevant document found."

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
