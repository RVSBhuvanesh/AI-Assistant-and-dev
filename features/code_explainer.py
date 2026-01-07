from core.ai_client import generate_response

def explain_code(code: str) -> str:
    prompt = f"""
You are an experienced software engineer and instructor.

Explain the following code clearly for a beginner.

Code:
{code}

Explanation must include:
- What the code does
- Key logic blocks
- Important functions or statements
- Simple language (no jargon)
"""
    return generate_response(prompt)
