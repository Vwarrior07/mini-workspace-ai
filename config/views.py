from django.shortcuts import render
from documents.models import Document
from runs.models import Run


def home(request):
    total_documents = Document.objects.count()
    total_runs = Run.objects.count()

    return render(request, "home.html", {
        "total_documents": total_documents,
        "total_runs": total_runs
    })
