from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

resume_chunks = []
resume_embeddings = []

def store_resume_text(text):

    global resume_chunks, resume_embeddings

    resume_chunks = text.split("\n")

    resume_embeddings = model.encode(resume_chunks)

def ask_question(question):

    question_embedding = model.encode([question])

    similarities = cosine_similarity(question_embedding, resume_embeddings)[0]

    best_index = similarities.argmax()

    return resume_chunks[best_index]