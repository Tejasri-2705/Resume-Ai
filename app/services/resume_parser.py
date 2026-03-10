import re

skills_list = [
    "python",
    "java",
    "machine learning",
    "sql",
    "mongodb",
    "react",
    "javascript"
]

def extract_email(text):
    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return email[0] if email else None


def extract_phone(text):
    phone = re.findall(r"\+?\d[\d -]{8,12}\d", text)
    return phone[0] if phone else None


def extract_skills(text):
    found_skills = []
    text_lower = text.lower()

    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)

    return found_skills


def parse_resume(text):
    return {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }