from core.ai_client import generate_response

def debug_code(code):
    prompt = f"""
You are an expert Python debugger and software engineer.

Analyze the given code and provide:

1. Errors in the code (if any)
2. Explanation of each error
3. Corrected version of the code
4. Suggestions to improve code quality

Make the explanation clear and beginner-friendly.

Code:
{code}
"""

    response = generate_response(prompt)
    return response
