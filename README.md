# AI Resume Analyzer

An AI-powered application that analyzes a candidate's resume against a job description using Google Gemini.

The application extracts text from PDF resumes, compares it with a Job Description (JD), identifies missing skills, evaluates resume-job matching, and generates interview questions.

You can run the app via the terminal for quick testing, or use the Streamlit interface for a better interactive experience

---

## Why I built this project
While searching for internship opportunities, I realized that every company has different skill requirements, and manually tailoring my CV for each job description is quite time-consuming.

Therefore, I developed the AI Resume Analyzer to help candidates analyze their CVs, identify missing skills, and better prepare before applying for positions.

## Features

- Read Resume from PDF
- CV Summary
- Analyze Job Description
- Comparing CVs and Job Descriptions
- Assess suitability
- Analyze the candidate's strengths and weaknesses
- List existing skills and identify missing ones
- Provide suggestions for improving the resume
- Generate interview questions using AI

---

## Tech Stack

- Python 3.13
- Google Gemini API
- PyPDF
- Python-dotenv
- Streamlit
---

## Project Structure

```
AI_Resume_Agent/
│
├── .venv
├── data/
│   └── cv.pdf
│
├── .env
├── .gitignore
├── create_prompt.py    # Prompt template
├── main.py             # Command-line version
├── app.py              # Streamlit Web UI
├── README.md
└── requirements.txt
```

## Roadmap

- [x] Read CVs from PDFs
- [x] Analyze job descriptions (JDs)
- [x] Compare CVs with JDs
- [x] Generate interview questions
- [x] Streamlit interface
- [x] Upload multiple CVs
- [ ] Export PDF reports
- [ ] AI agent workflow

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/ProjectsAI-Resume-Agent.git
```
Navigate to the project directory:

```bash
cd AI-Resume-Analyzer
```
---

### Create virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate.bat
```

---
### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure environment variables

Create a `.env` file in the project root and add your Gemini API key:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

You can obtain an API key from **Google AI Studio**.

---

### Prepare your resume

Place your resume PDF inside the `data` folder:

```text
data/
└── cv.pdf
```

---

### Run the application 
#### Option 1: Command Line Interface (CLI)
Run the application from the terminal:
```bash
python main.py
```
The application will prompt you to enter the path to your resume PDF, then analyze it against the predefined Job Description.

Example:

Enter the path to your resume data/(PDF): data/cv.pdf

#### Option 2: Streamlit Web Application

Launch the Streamlit application:

```bash
streamlit run app.py
```
Once the server starts, open your browser and navigate to:

http://localhost:8501

Using the web interface:

- Upload your resume in PDF format.
- Paste or enter the Job Description.
- Click Analyze.
- View the AI-generated analysis, including:
+ Resume summary
+ Resume-job matching score
+ Existing and missing skills
+ Strengths and weaknesses
+ Suggestions for improvement
+ Interview questions

## Example Output

text
Resume Match Score: 4/10

Strengths
- Flutter
- SQL
- Git

Missing Skills
- Python
- Prompt Engineering
- Agentic Frameworks/Models

Suggestions
- Learn Python
- Build AI projects
- Improve GitHub portfolio

Interview Questions

---

## Future Improvements

- Upload Resume directly
- Support DOCX
- Export Analysis Report
- JSON Output
- Multiple Resume Comparison

---

## Author

Huynh Thanh Phong

University of Information Technology - VNUHCM

Interests:
- AI Engineering
- Development
- Flutter
- Agentic AI

Email:
huynhthanhphongdev@gmail.com