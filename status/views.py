from django.http import JsonResponse
from django.db import connection
from django.conf import settings
from groq import Groq


def health_status(request):
    status = {
        "backend": "ok",
        "database": "unknown",
        "llm": "unknown"
    }

    # Check database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        status["database"] = "connected"
    except Exception:
        status["database"] = "error"

    # Check LLM connection
    try:
        client = Groq(api_key=settings.GROQ_API_KEY)

        # Simple lightweight test
        client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "ping"}],
            max_tokens=1
        )

        status["llm"] = "connected"

    except Exception:
        status["llm"] = "error"

    return JsonResponse(status)
