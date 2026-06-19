"""
utils/embeddings.py
-------------------
Provides semantic embedding and similarity functions using sentence-transformers.

Why sentence-transformers?
  - Free, runs locally, no API needed
  - Great for resume ↔ job description matching
  - The 'all-MiniLM-L6-v2' model is fast and accurate for this use case

Usage:
  embedding = get_embedding("Python developer with ML experience")
  score = cosine_similarity_score(embedding_a, embedding_b)
"""

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# ─── Load Model (Cached) ──────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def load_model():
    """
    Load the sentence transformer model once and cache it.
    'all-MiniLM-L6-v2' is small (80MB), fast, and works well for short texts.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str) -> np.ndarray:
    """
    Convert text into a dense vector (embedding).
    The model outputs a 384-dimensional vector.
    """
    model = load_model()
    # encode() returns a numpy array
    embedding = model.encode([text], convert_to_numpy=True)
    return embedding[0]


def cosine_similarity_score(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """
    Compute cosine similarity between two embedding vectors.
    Returns a float between 0.0 (no match) and 1.0 (perfect match).
    """
    # cosine_similarity expects 2D arrays
    score = cosine_similarity([vec_a], [vec_b])[0][0]
    return float(score)


def batch_similarity(resume_text: str, job_descriptions: list[str]) -> list[float]:
    """
    Compare one resume against many job descriptions efficiently.
    Returns a list of similarity scores (0.0 to 1.0) in the same order.
    """
    model = load_model()
    # Encode all texts in one batch — much faster than one-by-one
    all_texts = [resume_text] + job_descriptions
    embeddings = model.encode(all_texts, convert_to_numpy=True)

    resume_embedding = embeddings[0]
    job_embeddings = embeddings[1:]

    scores = cosine_similarity([resume_embedding], job_embeddings)[0]
    return [float(s) for s in scores]
