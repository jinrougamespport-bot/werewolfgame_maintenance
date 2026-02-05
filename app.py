from flask import Flask, render_template
from flask_socketio import SocketIO

# static_url_pathを指定して静的ファイルの場所を確定させます
app = Flask(__name__, static_folder='static', template_folder='templates')
socketio = SocketIO(app, cors_allowed_origins="*")

# --- ブラウザでアクセスしたときに index.html を出す設定 ---
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # ポート1000で実行
    socketio.run(app, host='0.0.0.0', port=1000, debug=True)