from pathlib import Path

index = Path("index.html")
html = index.read_text(encoding="utf-8")
old = '<article class="timeline-item"><div class="timeline-meta">2018 – Present</div><div><h3>Producer / Project Manager / Indie Game Developer <span>• Retnuh Productions</span></h3><p>Lead an active distributed game-development team and have coordinated more than 15 contributors across programming, art, audio, writing, and voice work while designing systems, levels, UI, narrative, production workflows, technical documentation, testing processes, and publisher-facing materials.</p></div></article>'
new = '<article class="timeline-item"><div class="timeline-meta">2018 – Present</div><div><h3>Producer / Project Manager / Indie Game Developer <span>• Retnuh Productions</span></h3><p>Lead an active distributed game-development team and have coordinated more than 15 contributors across programming, art, audio, writing, and voice work while designing systems, levels, UI, narrative, production workflows, technical documentation, testing processes, and publisher-facing materials.</p><a class="business-link hopo-link" href="https://kidhop-o.com/" target="_blank" rel="noopener"><img src="Kid_Hop_O_Redux_idle_4x.gif" alt="Kid Hop-o idle animation" /><span>Visit Kid Hop-o</span></a></div></article>'
if old not in html:
    raise SystemExit("Expected Retnuh Productions experience block not found")
index.write_text(html.replace(old, new), encoding="utf-8")

css = Path("style.css")
styles = css.read_text(encoding="utf-8")
marker = '.business-link:hover span::after,\n.business-link:focus-visible span::after { transform: translate(1px, -1px); }\n'
addition = marker + '.business-link.hopo-link img { image-rendering: pixelated; }\n'
if marker not in styles:
    raise SystemExit("Expected business-link style marker not found")
css.write_text(styles.replace(marker, addition), encoding="utf-8")
