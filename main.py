import os
from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
from create_prompt import read_prompt
load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

cv_path = input("Enter the path to your resume data/(PDF) : ")
try:
 reader = PdfReader(cv_path)
except FileNotFoundError:
    print("Resume file not found.")
    exit()

cv = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        cv += page_text + "\n"



jd = """
Agentic Software Engineer Intern

Requirements:
- Python
- GitHub
- REST API
- Models
- Prompting
- Evaluation
- Data Pipelines
- English reading comprehension
"""

prompt = read_prompt(cv, jd)



response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

print(response.text)