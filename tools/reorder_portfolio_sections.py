from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

old_nav = '''      <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#software">Software & Data</a>
        <a href="#games">Games</a>
        <a href="#visual-work">Visual Work</a>
        <a href="#experience">Experience</a>
        <a href="#contact">Contact</a>
      </div>'''
new_nav = '''      <div class="nav-links">
        <a href="#about">About</a>
        <a href="#featured">Featured Work</a>
        <a href="#experience">Experience</a>
        <a href="#skills">Skills</a>
        <a href="#software">Software & Data</a>
        <a href="#games">Games</a>
        <a href="#visual-work">Visual Work</a>
        <a href="#contact">Contact</a>
      </div>'''
if old_nav not in html:
    raise SystemExit("Navigation block not found")
html = html.replace(old_nav, new_nav, 1)
html = html.replace('<a class="button primary" href="#software">View technical work</a>', '<a class="button primary" href="#featured">View featured work</a>', 1)

def section(section_id):
    pattern = rf'\n    <section class="card(?: intro-card)?" id="{re.escape(section_id)}">.*?\n    </section>'
    match = re.search(pattern, html, flags=re.S)
    if not match:
        raise SystemExit(f"Section not found: {section_id}")
    return match.group(0)

about = section("about")
skills = section("skills")
software = section("software")
experience = section("experience")

articles = re.findall(r'        <article class="project-tile.*?</article>', software, flags=re.S)
if len(articles) != 8:
    raise SystemExit(f"Expected 8 software project cards, found {len(articles)}")

featured_articles = "\n\n".join(articles[:2])
remaining_articles = "\n\n".join(articles[2:])

featured = f'''
    <section class="card" id="featured">
      <div class="section-heading-row">
        <div><p class="section-kicker">Featured work</p><h2>Featured Technical Projects</h2></div>
        <p class="section-summary">Selected work connecting GIS and environmental data with gameplay programming and interactive systems.</p>
      </div>
      <div class="projects-grid featured-grid">
{featured_articles}
      </div>
    </section>'''

more_software = f'''
    <section class="card" id="software">
      <div class="section-heading-row">
        <div><p class="section-kicker">Additional technical work</p><h2>Software & Data Projects</h2></div>
        <p class="section-summary">Coursework and deployed projects demonstrating programming fundamentals, responsive web development, APIs, and AI-assisted development.</p>
      </div>
      <div class="projects-grid featured-grid">
{remaining_articles}
      </div>
    </section>'''

# Remove the three sections that are being repositioned/rebuilt.
for block in (skills, software, experience):
    html = html.replace(block, "", 1)

# Place the new hierarchy immediately after About.
new_stack = about + "\n" + featured + "\n" + experience + "\n" + skills + "\n" + more_software
if about not in html:
    raise SystemExit("About section disappeared during rewrite")
html = html.replace(about, new_stack, 1)

# Collapse excessive blank lines caused by moving whole sections.
html = re.sub(r'\n{4,}', '\n\n\n', html)
path.write_text(html, encoding="utf-8")
