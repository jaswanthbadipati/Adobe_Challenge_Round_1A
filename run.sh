#!/bin/bash

echo "📄 Running PDF Outline Extractor..."

# Create output directory if it doesn't exist
mkdir -p /app/output

# Run Python script
python3 Outline_Extractor.py --input_dir /app/input --output_dir /app/output --schema_path schema/outline.schema.json
