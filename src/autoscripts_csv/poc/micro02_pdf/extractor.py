from pathlib import Path

import pdfplumber


def extract_text_from_pdf(pdf_path: Path) -> str:
    text_blocks = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            text_blocks.append(f"--- page {i} ---\n{text}")

    return "\n".join(text_blocks)
