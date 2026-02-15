from django.shortcuts import render
from documents.models import Document
from .services import generate_answer


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
            max_score = 0

            # Break question into words
            question_words = set(question.lower().split())

            for doc in documents:
                content_words = set(doc.content.lower().split())
                score = len(question_words.intersection(content_words))

                if score > max_score:
                    max_score = score
                    best_doc = doc

            if best_doc and max_score > 0:
                context = best_doc.content[:2000]  # limit context size
                answer = generate_answer(question, context)
                source_document = best_doc.name
                excerpt = context[:300]
            else:
                answer = "No relevant document found."

    return render(request, "qa/ask.html", {
        "answer": answer,
        "source_document": source_document,
        "excerpt": excerpt
    })
