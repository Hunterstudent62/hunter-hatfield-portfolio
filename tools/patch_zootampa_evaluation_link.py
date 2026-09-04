from pathlib import Path

index = Path("index.html")
html = index.read_text(encoding="utf-8")
old = '<article class="timeline-item"><div class="timeline-meta">May – Aug 2026</div><div><h3>Animal Nutrition Intern <span>• ZooTampa at Lowry Park</span></h3><p>Prepared and distributed species-specific diets using written diet sheets and digital scales, supported high-volume nutrition-center operations, maintained feeder insects, followed sanitation and quality-control procedures, and gained introductory exposure to ZIMS, Zoo Diet NaviGator, Power BI, animal behavior, enrichment, welfare, and cooperative-care concepts. Completed a Cuban iguana nutrition research summary for staff.</p></div></article>'
new = '<article class="timeline-item"><div class="timeline-meta">May – Aug 2026</div><div><h3>Animal Nutrition Intern <span>• ZooTampa at Lowry Park</span></h3><p>Prepared and distributed species-specific diets using written diet sheets and digital scales, supported high-volume nutrition-center operations, maintained feeder insects, followed sanitation and quality-control procedures, and gained introductory exposure to ZIMS, Zoo Diet NaviGator, Power BI, animal behavior, enrichment, welfare, and cooperative-care concepts. Completed a Cuban iguana nutrition research summary for staff.</p><a class="evaluation-link" href="assets/Adobe%20Scan%20Aug%2020,%202026.pdf" target="_blank" rel="noopener"><span class="evaluation-filetype" aria-hidden="true">PDF</span><span>View internship evaluation</span></a></div></article>'
if old not in html:
    raise SystemExit("Expected ZooTampa experience block not found")
index.write_text(html.replace(old, new), encoding="utf-8")

css = Path("style.css")
styles = css.read_text(encoding="utf-8")
marker = '.business-link:focus-visible { outline: 2px solid var(--gold); outline-offset: 5px; border-radius: 4px; }\n'
addition = marker + '''.evaluation-link {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-top: 15px;
  color: var(--green-dark);
  text-decoration: none;
  font-size: .86rem;
  font-weight: 700;
  letter-spacing: .01em;
}
.evaluation-filetype {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 30px;
  border: 1px solid var(--border);
  border-radius: 5px;
  background: var(--soft);
  color: var(--muted);
  font-size: .68rem;
  font-weight: 800;
  letter-spacing: .06em;
}
.evaluation-link > span:last-child::after {
  content: "↗";
  margin-left: 7px;
  font-size: .82em;
  color: var(--muted);
}
.evaluation-link:hover > span:last-child,
.evaluation-link:focus-visible > span:last-child { text-decoration: underline; text-underline-offset: 3px; }
.evaluation-link:focus-visible { outline: 2px solid var(--gold); outline-offset: 5px; border-radius: 4px; }
'''
if marker not in styles:
    raise SystemExit("Expected business-link focus style not found")
css.write_text(styles.replace(marker, addition), encoding="utf-8")
