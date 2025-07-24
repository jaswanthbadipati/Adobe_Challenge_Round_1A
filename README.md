
# Round 1A - PDF Outline Extractor

## How to Run (Docker)

```bash
docker build -t round1a .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output round1a
```

## Output

The output will be a structured JSON with title and headings (H1 to H4) including page numbers.
