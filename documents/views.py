from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import DocumentUploadForm
from .models import Document

def upload_document(request):
    error = None

    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES["file"]

            if not uploaded_file.name.endswith(".txt"):
                error = "Only .txt files are allowed."
            else:
                content = uploaded_file.read().decode("utf-8")

                Document.objects.create(
                    name=uploaded_file.name,
                    content=content
                )

                return redirect("document_list")
    else:
        form = DocumentUploadForm()

    return render(request, "documents/upload.html", {
        "form": form,
        "error": error
    })


def document_list(request):
    documents = Document.objects.all().order_by("-created_at")

    return render(request, "documents/list.html", {
        "documents": documents
    })
