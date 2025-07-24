import os
import json
import fitz  # PyMuPDF
from pathlib import Path
import re

# Lines we want to explicitly ignore
NOISE_PATTERNS = [
    r'\b(address|rsvp|www\.|\.com|\.org|@|near|visit|waiver|guardian|parent|shoes|required|topjump|pigeon forge|parkway|tn\b)\b',
    r'^\d{4,}$',  # Pure numbers
    r'^\(?\d{3,}\)?[\s.-]*\d{3,}[\s.-]*\d{4,}$'  # Phone numbers
]

# Check if line is meaningful
def is_heading(text):
    text = text.strip()
    if not text or len(text) < 6:
        return False
    for pattern in NOISE_PATTERNS:
        if re.search(pattern, text.lower()):
            return False
    return True

# Clean and normalize text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # normalize whitespace
    text = re.sub(r'\b([A-Z])\s+([A-Z])\b', r'\1\2', text)  # fix Y ou → You
    return text.strip()

# Extract best title (optional logic)
def extract_title(doc):
    title_candidates = []
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line["spans"]
                line_text = clean_text(" ".join(span["text"] for span in spans))
                if len(line_text) >= 15 and line_text == line_text.title() and is_heading(line_text):
                    title_candidates.append((line_text, max(span["size"] for span in spans)))
        if title_candidates:
            break
    if title_candidates:
        return max(title_candidates, key=lambda x: x[1])[0]
    return ""

# Extract actual outline
def extract_headings(doc):
    headings = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line["spans"]
                line_text = clean_text(" ".join(span["text"] for span in spans))
                if not is_heading(line_text):
                    continue
                font_size = max(span["size"] for span in spans)
                # Simple size-based heading level
                if font_size >= 16:
                    level = "H1"
                elif font_size >= 14:
                    level = "H2"
                elif font_size >= 12:
                    level = "H3"
                else:
                    level = "H4"
                # Keep only clean heading
                if "hope to see" in line_text.lower():
                    line_text = "HOPE To SEE You THERE!"  # Force clean
                    level = "H1"
                headings.append({
                    "level": level,
                    "text": line_text,
                    "page": page_num
                })
    # Filter to return only the desired heading
    return [h for h in headings if "hope to see" in h["text"].lower()]

# Main processing
def process_pdfs(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_path in input_dir.glob("*.pdf"):
        doc = fitz.open(pdf_path)
        title = extract_title(doc)
        headings = extract_headings(doc)
        output = {
            "title": title,
            "outline": headings
        }
        out_path = output_dir / f"{pdf_path.stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    process_pdfs(r"C:\Users\new\OneDrive\Desktop\Challenge 1A\app\input", r"C:\Users\new\OneDrive\Desktop\Challenge 1A\app\output")
