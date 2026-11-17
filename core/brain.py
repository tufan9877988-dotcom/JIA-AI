import os
from google import genai
from core.voice import speak

def ask_jia(question):
    api_key = os.getenv("JIA_API_KEY")
    model_name = os.getenv("JIA_MODEL", "gemini-3.8-flash")

    if not api_key:
        return "JIA API Key is missing. Please configure it."

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=model_name,
            contents=question
        )

        answer = response.text

        if not answer:
            return "JIA received an empty response."

        try:
            speak(answer)
        except Exception as voice_error:
            print("Voice Error:", voice_error)

        return answer

    except Exception as error:
        return f"JIA Error: {error}"
