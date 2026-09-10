from pathlib import Path

index_path = Path("index.html")
css_path = Path("style.css")

html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Add Writing to the primary navigation.
nav_old = '''        <a href="#software">Software & Data</a>\n        <a href="#games">Games</a>'''
nav_new = '''        <a href="#software">Software & Data</a>\n        <a href="#writing">Writing</a>\n        <a href="#games">Games</a>'''
if nav_old not in html:
    raise SystemExit("Navigation anchor not found; refusing to patch.")
html = html.replace(nav_old, nav_new, 1)

# Strengthen the featured GIS description and add the report alongside the dashboard/repository actions.
gis_desc_old = '''            <p>Cleaning and standardizing public occurrence records for invasive and nonnative reptiles in Florida, then building species- and county-level maps and an interactive dashboard to examine distribution and reporting patterns.</p>'''
gis_desc_new = '''            <p>Independent GIS and environmental-data project examining 55,033 EDDMapS records for five nonnative reptile species in Florida from 2010–2025. I cleaned and mapped the data in QGIS, built an interactive Power BI dashboard, and wrote a research report combining the statewide analysis with field observations and reptile-husbandry case studies.</p>'''
if gis_desc_old not in html:
    raise SystemExit("Featured GIS description not found; refusing to patch.")
html = html.replace(gis_desc_old, gis_desc_new, 1)

gis_links_old = '''          <div class="link-row">\n            <a href="https://github.com/Hunterstudent62/Florida-Invasive-Reptiles" target="_blank" rel="noopener">GitHub project</a>\n            <a href="https://app.powerbi.com/view?r=eyJrIjoiMzJkNjRkMjEtZDQ1Yy00Yzg1LWIwNDEtZTNhNzE1NmYxNDU2IiwidCI6IjMyYjQ1YzdmLTMzYWUtNDM1OC04ZjMxLWVlMjIzNTAyYmYzOSJ9&amp;pageName=be560df123103ce50309" target="_blank" rel="noopener">Interactive Power BI dashboard</a>\n          </div>'''
gis_links_new = '''          <div class="link-row">\n            <a href="Florida_Nonnative_Reptiles_Project_Paper.pdf" target="_blank" rel="noopener">Read project report</a>\n            <a href="https://app.powerbi.com/view?r=eyJrIjoiMzJkNjRkMjEtZDQ1Yy00Yzg1LWIwNDEtZTNhNzE1NmYxNDU2IiwidCI6IjMyYjQ1YzdmLTMzYWUtNDM1OC04ZjMxLWVlMjIzNTAyYmYzOSJ9&amp;pageName=be560df123103ce50309" target="_blank" rel="noopener">Interactive Power BI dashboard</a>\n            <a href="https://github.com/Hunterstudent62/Florida-Invasive-Reptiles" target="_blank" rel="noopener">GitHub project</a>\n          </div>'''
if gis_links_old not in html:
    raise SystemExit("Featured GIS link row not found; refusing to patch.")
html = html.replace(gis_links_old, gis_links_new, 1)

# Insert Research & Technical Writing before Game Development.
games_anchor = '''\n\n    <section class="card" id="games">'''
writing_section = '''

    <section class="card" id="writing">
      <div class="section-heading-row">
        <div><p class="section-kicker">Research & writing</p><h2>Research & Technical Writing</h2></div>
        <p class="section-summary">Selected academic and applied research connecting GIS, zoo nutrition, mathematics, ecology, and technical communication.</p>
      </div>
      <div class="projects-grid research-grid">
        <article class="project-tile research-card">
          <div>
            <div class="tag-row"><span class="tag">GIS</span><span class="tag">Environmental Data</span><span class="tag">Field Study</span></div>
            <h3>Florida Nonnative Reptiles: Distribution, Establishment, Husbandry, and Management</h3>
            <p>Independent portfolio report combining a 55,033-record EDDMapS analysis with QGIS mapping, Power BI exploration, data-quality discussion, and two case studies: long-term tegu husbandry and a Tampa field study of Peter's rock agamas that included live capture of a juvenile.</p>
          </div>
          <a href="Florida_Nonnative_Reptiles_Project_Paper.pdf" target="_blank" rel="noopener">Read project report</a>
        </article>

        <article class="project-tile research-card">
          <div>
            <div class="tag-row"><span class="tag">Zoo Nutrition</span><span class="tag">Literature Review</span><span class="tag">Zoo Diet NaviGator</span></div>
            <h3>Cuban Iguana Diet Analysis</h3>
            <p>ZooTampa internship research presentation comparing a Cuban iguana's current diet with published wild-diet literature and other captive diets. The analysis uses Zoo Diet NaviGator to compare broad nutrient trends, documents important limitations, and proposes cautious husbandry recommendations.</p>
          </div>
          <a href="Diet%20Analysis%20Presentation%20final%20cleaned.pdf" target="_blank" rel="noopener">View research presentation</a>
        </article>

        <article class="project-tile research-card">
          <div>
            <div class="tag-row"><span class="tag">Calculus III</span><span class="tag">Vectors</span><span class="tag">Biomechanics</span></div>
            <h3>Calculus III and the Mathematics of Insect Flight</h3>
            <p>Course paper connecting vector-valued functions, velocity and acceleration, force vectors, and vector fields to insect flight, with examples from inverted landing maneuvers, flapping-wing aerodynamics, airflow, and biologically inspired robotics.</p>
          </div>
          <a href="Calc%203%20EC%20paper%20Insect%20Flight.pdf" target="_blank" rel="noopener">Read course paper</a>
        </article>
      </div>
    </section>'''
if games_anchor not in html:
    raise SystemExit("Game Development section anchor not found; refusing to patch.")
html = html.replace(games_anchor, writing_section + games_anchor, 1)

# Add a three-column writing grid that collapses cleanly on smaller screens.
css_anchor = '''.game-grid { grid-template-columns: repeat(3, 1fr); }'''
css_new = '''.research-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }\n.research-card { min-height: 290px; }\n.research-card h3 { line-height: 1.3; }\n\n.game-grid { grid-template-columns: repeat(3, 1fr); }'''
if css_anchor not in css:
    raise SystemExit("Primary CSS insertion anchor not found; refusing to patch.")
css = css.replace(css_anchor, css_new, 1)

media_anchor = '''  .game-grid { grid-template-columns: 1fr 1fr; }'''
media_new = '''  .game-grid,\n  .research-grid { grid-template-columns: 1fr 1fr; }'''
if media_anchor not in css:
    raise SystemExit("900px media-query anchor not found; refusing to patch.")
css = css.replace(media_anchor, media_new, 1)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
