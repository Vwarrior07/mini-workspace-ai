from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import DocumentUploadForm
from .models import Document

from pypdf import PdfReader
import io

def upload_document(request):
    error = None

    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES["file"]
            filename = uploaded_file.name

            if filename.endswith(".txt"):
                content = uploaded_file.read().decode("utf-8")

            elif filename.endswith(".pdf"):
                pdf_file = io.BytesIO(uploaded_file.read())
                reader = PdfReader(pdf_file)
                content = ""

                for page in reader.pages:
                    content += page.extract_text() or ""

            else:
                error = "Only .txt and .pdf files are allowed."
                return render(request, "documents/upload.html", {
                    "form": form,
                    "error": error
                })

            Document.objects.create(
                name=filename,
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
