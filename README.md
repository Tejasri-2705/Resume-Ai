# ResumeIQ – AI-Powered ATS Resume Analyzer

ResumeIQ is an AI-powered Applicant Tracking System (ATS) Resume Analyzer built using Python, Streamlit, and Google's Gemini API. It analyzes a resume against a job description and provides an ATS compatibility score, strengths, weaknesses, and recommendations for improvement.

## Features

- Upload resumes in PDF, DOCX, or TXT format.
- Analyze resumes against a job description.
- Generate an ATS compatibility score using Gemini AI.
- Identify resume strengths and weaknesses.
- Provide actionable recommendations to improve the resume.
- Download the analysis results as a JSON file.
- Interactive web interface built with Streamlit.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF
- Python-docx
- Pydantic

## Project Structure

```text
resumeiq-ats-analyzer/
├── app.py
├── requirements.txt
└── README.md
```

## Prerequisites

Before running the project, install or prepare:

- Python 3.10 or later
- pip (Python package manager)
- A Google Gemini API key
- Git (optional, for cloning the repository)

## How to Run the Project Locally

### Step 1: Clone the repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/YOUR_USERNAME/resumeiq-ats-analyzer.git
cd resumeiq-ats-analyzer
```

Replace `YOUR_USERNAME` with your GitHub username. Alternatively, download the repository as a ZIP file and extract it.

### Step 2: Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Gemini API key

Create a file named `.streamlit/secrets.toml` in the project directory.

Add the following configuration:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

**Security note:** Never upload your API key or `secrets.toml` file to GitHub. Add `.streamlit/secrets.toml` and `venv/` to your `.gitignore` file.

### Step 5: Run the application

From the project directory, execute:

```bash
streamlit run app.py
```

Streamlit will start a local web server. Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

### Step 6: Analyze a resume

1. Open ResumeIQ in your browser.
2. Upload a resume in PDF, DOCX, or TXT format.
3. Paste the target job description into the text area.
4. Click **Analyze Resume**.
5. Review the ATS score, strengths, weaknesses, and improvement recommendations.
6. Download the analysis results as a JSON file if needed.

## How to Run in Google Colab

If you are running the project in Google Colab, upload `app.py` and `requirements.txt` to your Colab session.

Install the dependencies:

```python
!pip install -r requirements.txt
```

Configure your API key using Colab Secrets. First, add a secret named `api_key` in the Colab Secrets panel and grant notebook access to it.

```python
from google.colab import userdata
import os

os.environ["GEMINI_API_KEY"] = userdata.get("api_key")
```

Start the Streamlit application:

```python
!streamlit run app.py --server.port 8501 \
  --server.headless true \
  --server.enableCORS false \
  --server.enableXsrfProtection false
```

For temporary Colab preview only, use a supported port-forwarding or preview method to open the application. The CORS and XSRF settings above are for troubleshooting a temporary notebook preview; do not disable these protections for a public deployment.

## Deployment on Streamlit Community Cloud

1. Push `app.py`, `requirements.txt`, and `README.md` to a GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub and create a new app.
4. Select your repository, branch, and `app.py` as the main file.
5. Open the app's **Settings → Secrets** section.
6. Add the following secret:

   ```toml
   GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
   ```

7. Save the secret and deploy the application.
8. Open the generated public URL and test the resume upload and analysis workflow.

Keep the API key private and do not commit it to the repository.

## Important Notes

- An internet connection is required for Gemini API requests.
- API access, quotas, and usage limits depend on your Google AI account.
- The generated ATS score is an AI-based estimate, not a guarantee of passing an employer's ATS screening.
- Review AI-generated recommendations before using them to modify a resume.

## Future Enhancements

- Resume-to-job keyword matching.
- Missing-skill identification.
- Multiple resume comparison.
- Resume improvement suggestions based on specific job roles.
- Downloadable PDF reports.

## Author

Developed as a Python and Generative AI project demonstrating resume analysis, API integration, and web application development.
