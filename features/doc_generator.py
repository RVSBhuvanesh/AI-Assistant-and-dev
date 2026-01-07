from core.ai_client import generate_response

def generate_documentation(project_name: str, description: str) -> str:
    prompt = f"""
You are a professional technical writer.

Generate clear, structured documentation for the following project.

Project Name:
{project_name}

Project Description:
{description}

The documentation MUST include:
1. Overview
2. Problem Statement
3. Features
4. System Architecture (high-level)
5. Installation Steps
6. Usage Instructions
7. Future Enhancements

Write in a clear, academic but simple tone.
"""
    return generate_response(prompt)
