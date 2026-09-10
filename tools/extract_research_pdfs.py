from pathlib import Path
from pypdf import PdfReader

PDFS = {
    "Calc 3 EC paper Insect Flight.pdf": "tools/research_extracts/calc3_insect_flight.txt",
    "Diet Analysis Presentation final cleaned.pdf": "tools/research_extracts/cuban_iguana_diet_analysis.txt",
    "Florida_Nonnative_Reptiles_Project_Paper.pdf": "tools/research_extracts/florida_nonnative_reptiles.txt",
}

for pdf_path, output_path in PDFS.items():
    reader = PdfReader(pdf_path)
    chunks = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n===== PAGE {page_num} =====\n\n{text}")
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(chunks), encoding="utf-8")
