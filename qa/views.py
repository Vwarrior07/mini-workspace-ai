from django.shortcuts import render
from documents.models import Document
from .services import generate_answer

def ask_question(request):
    answer = None
    source_document = None
    excerpt = None

    if request.method == "POST":
        question = request.POST.get("question")

        documents = Document.objects.all()

        # Simple relevance search
        best_doc = None
        for doc in documents:
            if question.lower() in doc.content.lower():
                best_doc = doc
                break

        if best_doc:
            context = best_doc.content[:2000]  # limit size
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
