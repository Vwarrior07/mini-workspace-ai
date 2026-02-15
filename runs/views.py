from django.shortcuts import render
from .models import Run


def run_history(request):
    runs = Run.objects.all().order_by("-created_at")[:5]

    return render(request, "runs/history.html", {
        "runs": runs
    })
