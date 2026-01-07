from core.ai_client import generate_response

def generate_readme(project_name: str, description: str) -> str:
    prompt = f"""
You are a senior software engineer.

Generate a professional GitHub README.md for the following project.

Project Name:
{project_name}

Project Description:
{description}

The README must include:
- Project Title
- Description
- Features
- Tech Stack
- Installation
- Usage
- Future Improvements

Format the output in valid Markdown.
"""
    return generate_response(prompt)

