from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
import sys

app = QApplication(sys.argv)

window = QWebEngineView()
window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
window.page().setBackgroundColor(QColor(0, 0, 0, 0))

html = '''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{display:flex;justify-content:center;align-items:center;height:100vh;background:transparent;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.island{background:rgba(195,193,195,0.95);backdrop-filter:blur(20px);border-radius:25px;width:70px;height:25px;display:flex;align-items:center;justify-content:center;transition:all 0.4s cubic-bezier(0.36,0.66,0.04,1);box-shadow:0 8px 32px rgba(0,0,0,0.3)}
.island:hover{width:300px;height:45px}
.icon{width:25px;height:25px;background:url("https://i.imgur.com/8YAtaDK.png") center/cover;border-radius:50% 14px 45% 50%}
</style></head>
<body><div class="island"><div class="icon"></div></div></body>
</html>'''

window.setHtml(html)
window.setGeometry(800, 30, 400, 200)
window.show()

sys.exit(app.exec())
