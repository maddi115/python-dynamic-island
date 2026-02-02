import webview
import time
import threading
from screeninfo import get_monitors

class ComputationAPI:
    def __init__(self):
        self.window = None
        self.running = False
    
    def start_computation(self):
        if self.running:
            return 'Already running'
        self.running = True
        thread = threading.Thread(target=self._compute)
        thread.daemon = True
        thread.start()
        return 'Started'
    
    def _compute(self):
        for i in range(100):
            if not self.running:
                break
            time.sleep(0.05)
            result = i ** 2
            self.window.state.progress = i + 1
            self.window.state.result = result
        self.running = False
    
    def stop_computation(self):
        self.running = False
        return 'Stopped'

def create_html():
    return '''<!DOCTYPE html><html><head><meta charset="UTF-8"><style>*{margin:0;padding:0;box-sizing:border-box}body{display:flex;justify-content:center;align-items:center;height:100vh;margin:0;background:#f0f0f0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}section{perspective:1000px;position:relative}.island{background:#c3c1c3;border-radius:25px;width:70px;height:25px;display:flex;align-items:center;justify-content:center;transition:all 0.4s cubic-bezier(0.36,0.66,0.04,1);position:relative;-webkit-app-region:drag}.island:hover{width:300px;height:45px}.island.expanded{width:350px!important;height:150px!important;border-radius:30px!important}.default{position:absolute;width:25px;height:25px;background:url("https://i.imgur.com/8YAtaDK.png") center/cover;border-radius:50% 14px 45% 50%;transition:opacity 0.3s}.island:hover .default,.island.expanded .default{opacity:0}.apps{display:flex;gap:15px;opacity:0;transition:opacity 0.3s;position:absolute;-webkit-app-region:no-drag}.island:hover .apps{opacity:1}.island.expanded .apps{opacity:0}.app{width:19px;height:22px;background:#4a4a4a;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:all 0.3s;cursor:pointer;font-size:16px}.island:hover .app{width:35px;height:35px;font-size:20px}.app:hover{transform:scale(1.2)}.app.m{background:url("https://i.imgur.com/8YAtaDK.png") center/cover;border-radius:50% 14px 45% 50%}.view{display:none;flex-direction:column;align-items:center;gap:10px;padding:20px;position:absolute;top:0;left:0;right:0;bottom:0;-webkit-app-region:no-drag}.view.active{display:flex}.result{font-size:32px;color:#ff6b35;font-weight:bold}.bar{width:100%;height:8px;background:rgba(0,0,0,0.1);border-radius:10px;overflow:hidden}.fill{height:100%;background:#ff6b35;width:0%;transition:width 0.2s}.btns{display:flex;gap:10px}button{padding:8px 20px;border:none;border-radius:20px;font-size:13px;font-weight:600;cursor:pointer;background:#ff6b35;color:white}button:hover{transform:scale(1.05)}.back{background:#4a4a4a}</style></head><body><section><div class="island" id="i"><div class="default"></div><div class="apps"><div class="app m"></div><div class="app">📅</div><div class="app">🎵</div><div class="app">📷</div><div class="app" onclick="show()">⚙️</div></div><div class="view" id="v"><div class="result" id="r">0</div><div class="bar"><div class="fill" id="f"></div></div><div class="btns"><button onclick="start()">Start</button><button onclick="stop()">Stop</button><button class="back" onclick="hide()">Back</button></div></div></div></section><script>function show(){document.getElementById('i').classList.add('expanded');document.getElementById('v').classList.add('active')}function hide(){document.getElementById('i').classList.remove('expanded');document.getElementById('v').classList.remove('active')}async function start(){await pywebview.api.start_computation()}async function stop(){await pywebview.api.stop_computation()}window.addEventListener('pywebviewready',function(){setInterval(()=>{if(window.state){document.getElementById('r').textContent=window.state.result||'0';document.getElementById('f').style.width=(window.state.progress||0)+'%'}},50)})</script></body></html>'''

if __name__ == '__main__':
    api = ComputationAPI()
    monitor = get_monitors()[0]
    window_width = 400
    window_height = 200
    x = (monitor.width - window_width) // 2
    y = 30
    window = webview.create_window('Maddie',html=create_html(),width=window_width,height=window_height,x=x,y=y,frameless=True,on_top=True,resizable=False,js_api=api)
    api.window = window
    window.state.progress = 0
    window.state.result = 0
    webview.start(debug=True)
