from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

old_c = '''<article class="project-tile"><div><div class="tag-row"><span class="tag">C</span><span class="tag">Linked Lists</span><span class="tag">Dynamic Memory</span><span class="tag">Multi-file Design</span></div><h3>Tutor Directory</h3><p>A multi-file C command-line application built around structs, pointers, and a dynamically allocated linked list. It uses <code>malloc</code>/<code>free</code>, string handling, header files and include guards, sorted insertion, duplicate detection, preference-based search, record deletion, input validation, and complete cleanup of allocated nodes before exit.</p></div><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/tree/main/code-samples/c-tutor-directory" target="_blank" rel="noopener">View source & build notes</a></article>'''
new_c = '''<article class="project-tile"><div><div class="tag-row"><span class="tag">C</span><span class="tag">Linked Lists</span><span class="tag">Dynamic Memory</span><span class="tag">Multi-file Design</span></div><h3>Tutor Directory</h3><p>I built this command-line tutor directory for a C programming course. It uses a linked list to keep tutor records sorted by name and lets the user add, search, and delete records. As the assignment grew, I split the program across source and header files and got hands-on practice with pointers, <code>malloc</code>/<code>free</code>, duplicate checking, and cleaning up allocated memory before exit.</p></div><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/tree/main/code-samples/c-tutor-directory" target="_blank" rel="noopener">View source & build notes</a></article>'''

old_java = '''<article class="project-tile"><div><div class="tag-row"><span class="tag">Java</span><span class="tag">2D Arrays</span><span class="tag">Animal Data</span></div><h3>Poultry Production Tracker</h3><p>A Java coursework application for tracking egg production across individual birds and weeks. It validates input, calculates totals and weekly averages, and identifies the highest producer.</p></div><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/tree/main/code-samples/java-poultry-tracker" target="_blank" rel="noopener">View source & project notes</a></article>'''
new_java = '''<article class="project-tile"><div><div class="tag-row"><span class="tag">Java</span><span class="tag">2D Arrays</span><span class="tag">Animal Data</span></div><h3>Poultry Production Tracker</h3><p>I built this Java console program for a class assignment to track egg production for a small flock over multiple weeks. It stores each chicken's weekly production in a two-dimensional array, then calculates totals and averages and reports the highest-producing bird. I later cleaned up the input handling and summary output for the portfolio version.</p></div><a href="https://github.com/Hunterstudent62/hunter-hatfield-portfolio/tree/main/code-samples/java-poultry-tracker" target="_blank" rel="noopener">View source & project notes</a></article>'''

if old_c not in html:
    raise SystemExit('Tutor Directory block not found')
if old_java not in html:
    raise SystemExit('Poultry Production Tracker block not found')

html = html.replace(old_c, new_c).replace(old_java, new_java)
path.write_text(html, encoding='utf-8')
