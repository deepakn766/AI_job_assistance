"""
utils/parser.py
---------------
Handles raw text extraction from uploaded resume files.

Supports:
  - PDF  (via pdfplumber)
  - DOCX (via python-docx)

Returns plain text that other agents will process further.
"""

import pdfplumber
import docx
import re


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract all text from a PDF file page by page.
    pdfplumber handles most resume PDF formats reliably.
    """
    text_parts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    return "\n".join(text_parts)


def extract_text_from_docx(file_path: str) -> str:
    """
    Extract all paragraph text from a DOCX file.
    python-docx reads each paragraph in order.
    """
    doc = docx.Document(file_path)
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(paragraphs)


def extract_text(file_path: str) -> str:
    """
    Route to the correct extractor based on file extension.
    Returns raw resume text.
    """
    file_path_lower = file_path.lower()
    if file_path_lower.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path_lower.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}. Use PDF or DOCX.")


# ─── Quick Regex Helpers ──────────────────────────────────────────────────────

def extract_email(text: str) -> str:
    """Find the first email address in the text."""
    pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else ""


def extract_phone(text: str) -> str:
    """Find the first phone number in the text."""
    pattern = r"(\+?\d[\d\s\-().]{7,}\d)"
    match = re.search(pattern, text)
    return match.group(0).strip() if match else ""


def extract_name_heuristic(text: str) -> str:
    """
    Simple heuristic: the candidate's name is usually in the first 1-3 lines.
    We grab the first non-empty line that looks like a name (no @ or digits).
    """
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    for line in lines[:5]:
        # Skip lines that look like contact info or headers
        if "@" in line or any(c.isdigit() for c in line):
            continue
        # A name is typically 2-4 words, all starting with caps
        words = line.split()
        if 2 <= len(words) <= 4 and all(w[0].isupper() for w in words if w):
            return line
    return lines[0] if lines else "Unknown"
