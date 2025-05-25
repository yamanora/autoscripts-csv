from pathlib import Path

from autoscripts_csv.poc.micro02_pdf.extractor import extract_text_from_pdf


def test_extract_text_from_pdf_normal_case():
    pdf_path = Path(__file__).parent / "fixtures" / "sample.pdf"
    result = extract_text_from_pdf(pdf_path)

    assert "Invoice" in result
    assert "Total amount: 123,456 yen" in result
    assert "--- page 1 ---" in result
