import sys
from pathlib import Path

import pdfplumber


def dump_text(pdf_path: Path) -> None:
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            print(f"\n--- page {i} ---\n{text}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("使い方: python extractor_proof_of_concept.py <PDFファイルのパス>")
    dump_text(Path(sys.argv[1]))
