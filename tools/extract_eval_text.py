from pathlib import Path
import subprocess
import tempfile

pdf = Path('assets/Adobe Scan Aug 20, 2026.pdf')
out = Path('tools/eval_extracted.txt')

# First try the OCR/text layer already embedded by Adobe Scan.
text = subprocess.run(['pdftotext', str(pdf), '-'], capture_output=True, text=True).stdout.strip()

# Fall back to OCR if the embedded layer is missing or nearly empty.
if len(text) < 200:
    with tempfile.TemporaryDirectory() as d:
        prefix = str(Path(d) / 'page')
        subprocess.run(['pdftoppm', '-r', '180', '-png', str(pdf), prefix], check=True)
        pages = []
        for image in sorted(Path(d).glob('page-*.png')):
            result = subprocess.run(['tesseract', str(image), 'stdout'], capture_output=True, text=True)
            pages.append(result.stdout)
        text = '\n\n--- PAGE BREAK ---\n\n'.join(pages)

out.write_text(text, encoding='utf-8')
print(text[:4000])
