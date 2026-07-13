import os
import streamlit as st

from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader

from create_prompt import read_prompt



load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



def extract_pdf(file):

    reader = PdfReader(file)

    cv = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            cv += page_text + "\n"

    return cv



# Giao diện
st.title("AI Resume Analyzer")


cv_file = st.file_uploader(
    "Upload your CV (PDF)",
    type="pdf"
)


jd = st.text_area(
    "Job Description",
    """
Agentic Software Engineer Intern

Requirements:
- Python
- GitHub
- REST API
- Models
- Prompting
- Evaluation
- Data Pipelines
"""
)


if st.button("Analyze"):

    if cv_file is None:

        st.warning("Please upload your CV")

    else:

      
        cv = extract_pdf(cv_file)

        prompt = read_prompt(cv, jd)


        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )


        st.markdown(response.text)