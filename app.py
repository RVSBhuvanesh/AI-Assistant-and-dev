import streamlit as st

from features.doc_generator import generate_documentation
from features.readme_generator import generate_readme
from features.code_explainer import explain_code

st.set_page_config(
    page_title="AI Assistant for Students & Developers",
    layout="wide"
)

# --- Header UI ---
st.title("🤖 AI Assistant for Students & Developers")
st.caption("🚀 Built with Python, Streamlit & Google Gemini")
st.divider()

st.write("Powered by Google Gemini")

tool = st.selectbox(
    "Select a tool",
    [
        "Documentation Generator",
        "README Generator",
        "Code Explainer"
    ]
)

st.divider()

# --- Tool Logic ---
if tool in ["Documentation Generator", "README Generator"]:
    project_name = st.text_input("Project Name")
    description = st.text_area("Project Description", height=200)

    if st.button("Generate"):
        if project_name and description:
            with st.spinner("Generating..."):
                if tool == "Documentation Generator":
                    result = generate_documentation(project_name, description)
                else:
                    result = generate_readme(project_name, description)

            st.subheader("Generated Output")
            st.markdown(result)
        else:
            st.warning("Please fill all fields")

elif tool == "Code Explainer":
    code = st.text_area("Paste your code here", height=250)

    if st.button("Explain Code"):
        if code.strip():
            with st.spinner("Analyzing code..."):
                result = explain_code(code)

            st.subheader("Code Explanation")
            st.markdown(result)
        else:
            st.warning("Please paste some code")
            
