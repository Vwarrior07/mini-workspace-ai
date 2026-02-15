from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_answer(question, context):
    prompt = f"""
    You are an expert research assistant.

    Your task:
    - Carefully read the provided context.
    - Provide a clear, well-structured answer.
    - Use complete sentences.
    - Include important supporting details from the context.
    - If multiple points exist, organize them in bullet points.
    - Do NOT make up information.
    - If the answer is not found in the context, respond with:
    "Answer not found in documents."

    Context:
    {context}

    Question:
    {question}
    """


    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Groq error:", str(e))  # <-- ADD THIS
        return f"LLM error: {str(e)}"
