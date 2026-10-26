# ResumeIQ: AI-Powered ATS Resume Analyzer

## Abstract

ResumeIQ is an AI-powered web application that evaluates a candidate's resume against a specific job description. It uses Google's Gemini generative AI API to estimate resume-job alignment and provide actionable feedback. The application identifies relevant strengths, missing or weakly demonstrated requirements, and suggested improvements to help candidates tailor their resumes.

## Objectives

- Automate preliminary resume-to-job-description comparison.
- Generate an approximate ATS-style match score.
- Identify relevant skills and requirements demonstrated in the resume.
- Highlight potential skill gaps.
- Provide actionable, truthful resume improvement suggestions.
- Present the analysis through an accessible web interface.

## Technologies Used

- **Programming language:** Python
- **Frontend and application framework:** Streamlit
- **Generative AI:** Google Gemini API
- **Structured data validation:** Pydantic
- **Document processing:** pypdf and python-docx
- **Development environment:** Google Colab
- **Deployment target:** Streamlit Community Cloud

## System Workflow

1. The user uploads a resume in PDF, DOCX, or TXT format.
2. The application extracts readable resume text.
3. The user supplies the target job description.
4. The extracted resume and job description are submitted to Gemini.
5. Gemini returns structured JSON containing the match score, summary, strengths, weaknesses, and recommendations.
6. Pydantic validates the returned response.
7. Streamlit displays the analysis in a user-friendly dashboard.
8. The user can download the analysis as a JSON file.

## Main Modules

**Resume Upload and Extraction:** Accepts supported document formats and extracts text for analysis.

**Job Description Input:** Collects the requirements and responsibilities of the target role.

**AI Analysis Engine:** Uses Gemini to compare resume evidence against the job description.

**Structured Output Validation:** Uses Pydantic to validate the AI response and enforce the expected score range.

**Results Dashboard:** Displays the estimated match score, summary, strengths, weaknesses, and recommendations.

**Report Export:** Allows the user to download the structured analysis as JSON.

## Expected Outcome

The application provides an interactive interface for preliminary resume screening and personalized feedback. It helps candidates understand how their documented qualifications align with a target role and what areas may need improvement.

## Limitations

- The match score is an AI-generated estimate, not an actual employer ATS score.
- The quality of feedback depends on the supplied resume, job description, and AI response.
- Scanned image-only PDFs may require OCR.
- The application does not independently verify candidate qualifications.
- Gemini API access, model availability, and usage limits affect operation.
- The application should not be used as the sole basis for employment decisions.

## Future Enhancements

- Keyword match visualization.
- Resume version comparison.
- Job-specific resume improvement suggestions.
- Analysis history and report management.
- Authentication and access controls.
- More detailed skill coverage reports.
