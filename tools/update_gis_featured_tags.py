from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")
old = '<div class="tag-row"><span class="tag">QGIS</span><span class="tag">Power BI</span><span class="tag">Python</span><span class="status">In progress</span></div>'
new = '<div class="tag-row"><span class="tag">QGIS</span><span class="tag">Power BI</span><span class="tag">Environmental Data</span><span class="tag">Field Study</span></div>'
if old not in text:
    raise SystemExit("Expected GIS tag row not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
