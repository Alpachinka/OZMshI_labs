"""Збирає index.html: вставляє Brain.js (base64) у шаблон, щоб сторінка працювала без сервера (подвійний клік)."""
import base64, pathlib
root = pathlib.Path(__file__).parent
lib = (root / "vendor" / "brain.browser.js").read_bytes()
tpl = (root / "src" / "app.template.html").read_text(encoding="utf-8")
tag = '<script>const BRAIN_B64="%s";</script>' % base64.b64encode(lib).decode()
(root / "index.html").write_text(tpl.replace("<!--BRAIN-->", tag), encoding="utf-8")
print("index.html зібрано:", round((root / "index.html").stat().st_size / 1e6, 2), "МБ")
