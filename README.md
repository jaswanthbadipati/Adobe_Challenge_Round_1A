
# Challenge 1A: PDF Outline Extraction Solution

## Overview
This repository contains a Dockerized solution for **Round 1A** of the Adobe India Hackathon 2025. The challenge involves extracting a structured outline (title, headings H1 to H4 with page numbers) from PDF files and saving them in JSON format.

## Solution Highlights
- Extracts **title** and **section headings (H1 to H4)** from PDFs
- Uses **PyMuPDF (fitz)** for fast and accurate PDF parsing
- Outputs one JSON file per input PDF
- Fully containerized with **Docker** and compliant with Adobe’s constraints

## Folder Structure

round-1a/
├── Dockerfile
├── requirements.txt
├── process\_pdfs.py
├── utils.py
├── input/
│   └── sample.pdf
├── output/
│   └── sample.json
└── README.md


## Requirements
- **No internet access during execution**
- **Run on CPU only** (amd64)
- **Process 50-page PDFs in ≤ 10 seconds**
- **Use ≤ 200MB for models/libraries**
- **Output format must match schema**
- **Input directory is read-only**
- All tools must be **open source**

## Build & Run Instructions

### Build Docker Image
```bash
docker build --platform linux/amd64 -t pdf-outline-extractor .
````

### Run Docker Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none pdf-outline-extractor
```

## Output Format

Each `filename.pdf` in `input/` generates `filename.json` in `output/`.

### Example Output:

```json
{
  "title": "South of France Travel Guide",
  "outline": [
    {
      "level": "H1",
      "text": "Things To Do",
      "page": 2
    },
    {
      "level": "H2",
      "text": "Outdoor Adventures",
      "page": 3
    },
    {
      "level": "H3",
      "text": "Kayaking",
      "page": 4
    },
    {
      "level": "H4",
      "text": "Equipment Rentals",
      "page": 5
    }
  ]
}
```

## Tech Stack

* Python 3.10
* [PyMuPDF (fitz)](https://pymupdf.readthedocs.io)
* Docker

## Tips for Improvement

* Use font size, boldness, and indentation to detect heading levels
* Eliminate noise like dates, addresses, and credits
* Fine-tune logic for better hierarchy detection

## Testing Your Build

```bash
docker run --rm \
  -v $(pwd)/sample_dataset/pdfs:/app/input:ro \
  -v $(pwd)/sample_dataset/outputs:/app/output \
  --network none pdf-outline-extractor
```

## License

This project uses only open-source tools and complies with Adobe Hackathon requirements.

```

</details>

---

Let me know if you want the same for **Round 1B**, or want both as downloadable `.md` files in a ZIP.
```
