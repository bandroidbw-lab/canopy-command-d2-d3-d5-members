from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('d2_master_board.html')
    except Exception as e:
        return f"Template Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)