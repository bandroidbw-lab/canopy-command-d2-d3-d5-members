from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
try:
    with open('d2_master_board.html', 'r') as f:
        return f.read()
except FileNotFoundError:
    return "Apex Timberline Operations - D2 Master Board Active"

if __name__ == '__main__':
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
