from core.ai_client import generate_response

if __name__ == "__main__":
    prompt = "Explain Git in simple terms for a beginner"
    result = generate_response(prompt)
    print(result)
