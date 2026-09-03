from pathlib import Path

index = Path("index.html")
html = index.read_text(encoding="utf-8")
old = '''      lightboxImage.src = image.src;
      lightboxImage.alt = image.alt;
      lightboxImage.style.background = image.src.includes("dk-sprite-sheet.png") ? "#1c1c1a" : "transparent";
      lightboxCaption.textContent = image.alt;'''
new = '''      lightboxImage.src = image.src;
      lightboxImage.alt = image.alt;
      const isDkSpriteSheet = image.src.includes("dk-sprite-sheet.png");
      const isDkPortraitSheet = image.src.includes("dk-expressions.png");
      lightboxImage.style.background = isDkSpriteSheet ? "#1c1c1a" : "transparent";
      lightboxImage.classList.toggle("large-preview", isDkSpriteSheet || isDkPortraitSheet);
      lightboxImage.classList.toggle("pixel-preview", isDkSpriteSheet);
      lightboxCaption.textContent = image.alt;'''
if old not in html:
    raise SystemExit("Expected lightbox JavaScript block not found")
index.write_text(html.replace(old, new), encoding="utf-8")

css = Path("style.css")
styles = css.read_text(encoding="utf-8")
old_content = '''.lightbox-content {
  max-width: min(1200px, 94vw);
  max-height: 90vh;'''
new_content = '''.lightbox-content {
  max-width: 96vw;
  max-height: 94vh;'''
if old_content not in styles:
    raise SystemExit("Expected lightbox-content block not found")
styles = styles.replace(old_content, new_content)
marker = '''.lightbox-caption {
  margin: 0;'''
addition = '''.lightbox-image.large-preview {
  width: min(1500px, 94vw);
  max-width: 94vw;
  max-height: 88vh;
}
.lightbox-image.pixel-preview {
  image-rendering: pixelated;
}

.lightbox-caption {
  margin: 0;'''
if marker not in styles:
    raise SystemExit("Expected lightbox-caption block not found")
css.write_text(styles.replace(marker, addition), encoding="utf-8")
