from pathlib import Path

import pytest

from autoscripts_csv.poc.micro02_pdf.cli import main


def test_cli_output(tmp_path, capsys):
    sample_pdf = Path(__file__).parent / "fixtures" / "sample.pdf"
    out_file = tmp_path / "result.txt"

    exit_code = main(["--pdf", str(sample_pdf), "--output", str(out_file)])
    assert exit_code == 0

    assert out_file.exists()
    text = out_file.read_text(encoding="utf-8")
    assert "Invoice" in text
    assert "Total amount" in text

    captured = capsys.readouterr()
    assert captured.out == ""


def test_missing_pdf_file(tmp_path, capsys):
    fake_pdf = tmp_path / "notfound.pdf"
    out_file = tmp_path / "result.txt"

    exit_code = main(["--pdf", str(fake_pdf), "--output", str(out_file)])

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "PDFファイルが見つかりません" in captured.err


def test_missing_pdf_arg(capsys):
    with pytest.raises(SystemExit) as exc:
        main([])

    assert exc.value.code == 2
    captured = capsys.readouterr()
    assert "usage:" in captured.err


def test_output_write_error(tmp_path, capsys):
    sample_pdf = Path(__file__).parent / "fixtures" / "sample.pdf"
    error_dir = tmp_path / "no_such_dir"
    out_file = error_dir / "output.txt"

    exit_code = main(["--pdf", str(sample_pdf), "--output", str(out_file)])

    # 書き込み失敗 → exit 2（想定外の例外）
    assert exit_code == 2

    captured = capsys.readouterr()
    assert "UNEXPECTED ERROR" in captured.err


def test_notify_called(tmp_path, mocker):
    mock = mocker.patch("autoscripts_csv.poc.micro02_pdf.cli.post_to_slack")

    sample_pdf = Path(__file__).parent / "fixtures" / "sample.pdf"
    out_file = tmp_path / "result.txt"

    exit_code = main(["--pdf", str(sample_pdf), "--output", str(out_file), "--notify"])
    assert exit_code == 0

    mock.assert_called_once()
