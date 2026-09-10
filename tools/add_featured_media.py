from pathlib import Path

index_path = Path("index.html")
css_path = Path("style.css")

html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

old_gis = '''        <article class="project-tile featured-project"><div><div class="tag-row"><span class="tag">QGIS</span><span class="tag">Power BI</span><span class="tag">Python</span><span class="status">In progress</span></div><h3>Florida Invasive Reptile GIS Dashboard</h3><p>Cleaning and standardizing public occurrence records for invasive and nonnative reptiles in Florida, then building species- and county-level maps and an interactive dashboard to examine distribution and reporting patterns.</p></div><p class="project-note">A portfolio project connecting computer science, GIS, environmental data, and my animal/conservation interests.</p></article>'''

new_gis = '''        <article class="project-tile featured-project">
          <div>
            <div class="tag-row"><span class="tag">QGIS</span><span class="tag">Power BI</span><span class="tag">Python</span><span class="status">In progress</span></div>
            <h3>Florida Invasive Reptile GIS Dashboard</h3>
            <p>Cleaning and standardizing public occurrence records for invasive and nonnative reptiles in Florida, then building species- and county-level maps and an interactive dashboard to examine distribution and reporting patterns.</p>
          </div>
          <div class="featured-media gis-media" aria-label="QGIS project maps">
            <figure>
              <img loading="lazy" src="assets/images/Species%20Occurence%20Map.png" alt="QGIS statewide species occurrence map for invasive and nonnative reptiles in Florida" />
              <figcaption>Species occurrence map</figcaption>
            </figure>
            <figure>
              <img loading="lazy" src="assets/images/County%20Occurrence%20Choropleth.png" alt="QGIS county occurrence choropleth for invasive and nonnative reptiles in Florida" />
              <figcaption>County occurrence choropleth</figcaption>
            </figure>
          </div>
          <p class="project-note">A portfolio project connecting computer science, GIS, environmental data, and my animal/conservation interests.</p>
          <div class="link-row">
            <a href="https://github.com/Hunterstudent62/Florida-Invasive-Reptiles" target="_blank" rel="noopener">GitHub project</a>
            <a href="https://app.powerbi.com/view?r=eyJrIjoiMzJkNjRkMjEtZDQ1Yy00Yzg1LWIwNDEtZTNhNzE1NmYxNDU2IiwidCI6IjMyYjQ1YzdmLTMzYWUtNDM1OC04ZjMxLWVlMjIzNTAyYmYzOSJ9&amp;pageName=be560df123103ce50309" target="_blank" rel="noopener">Interactive Power BI dashboard</a>
          </div>
        </article>'''

old_hopo = '''        <article class="project-tile featured-project"><div><div class="tag-row"><span class="tag">C#</span><span class="tag">Unity</span><span class="tag">Gameplay Systems</span></div><h3>Kid Hop-o Player Movement System</h3><p>An extensive Unity/C# controller for a momentum-focused platform RPG, supporting running, jumping, spin states, fluttering, wall interactions, ledge and vine behavior, custom air physics, animation synchronization, and runtime movement tuning.</p></div><div class="link-row"><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/tree/main/code-samples/kid-hopo-player-movement" target="_blank" rel="noopener">Architecture notes</a><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/blob/main/code-samples/kid-hopo-player-movement/CASE_STUDY.md" target="_blank" rel="noopener">Full case study</a></div></article>'''

new_hopo = '''        <article class="project-tile featured-project">
          <div>
            <div class="tag-row"><span class="tag">C#</span><span class="tag">Unity</span><span class="tag">Gameplay Systems</span></div>
            <h3>Kid Hop-o Player Movement System</h3>
            <p>An extensive Unity/C# controller for a momentum-focused platform RPG, supporting running, jumping, spin states, fluttering, wall interactions, ledge and vine behavior, custom air physics, animation synchronization, and runtime movement tuning.</p>
          </div>
          <div class="featured-video">
            <iframe src="https://www.youtube-nocookie.com/embed/_qF6yAWAuxc" title="Kid Hop-o trailer demonstrating player movement" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
          </div>
          <div class="link-row"><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/tree/main/code-samples/kid-hopo-player-movement" target="_blank" rel="noopener">Architecture notes</a><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/blob/main/code-samples/kid-hopo-player-movement/CASE_STUDY.md" target="_blank" rel="noopener">Full case study</a></div>
        </article>'''

for label, old, new in (("GIS featured card", old_gis, new_gis), ("Kid Hop-o featured card", old_hopo, new_hopo)):
    if old not in html:
        raise SystemExit(f"Expected {label} markup not found; refusing to patch.")
    html = html.replace(old, new, 1)

old_selector = 'const zoomTargets = document.querySelectorAll(".pipeline-visuals img, .pixel-asset-row img");'
new_selector = 'const zoomTargets = document.querySelectorAll(".pipeline-visuals img, .pixel-asset-row img, .featured-media img");'
if old_selector not in html:
    raise SystemExit("Expected lightbox selector not found; refusing to patch.")
html = html.replace(old_selector, new_selector, 1)

css_anchor = '''.link-row { display: flex; flex-wrap: wrap; gap: 14px; }\n\n.game-grid'''
css_insert = '''.link-row { display: flex; flex-wrap: wrap; gap: 14px; }

.featured-media {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px;
}
.featured-media figure {
  margin: 0;
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
}
.featured-media img {
  width: 100%;
  aspect-ratio: 16 / 10;
  display: block;
  object-fit: contain;
  background: #fff;
  cursor: zoom-in;
}
.featured-media figcaption {
  padding: 7px 9px;
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: .78rem;
  line-height: 1.35;
}
.featured-video {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #1d1d1b;
  border: 1px solid var(--border);
  border-radius: 10px;
}
.featured-video iframe {
  width: 100%;
  height: 100%;
  display: block;
  border: 0;
}

.game-grid'''
if css_anchor not in css:
    raise SystemExit("Expected CSS anchor not found; refusing to patch.")
css = css.replace(css_anchor, css_insert, 1)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
