<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask
>>>>>>> f23da3a424767cde9e133a6e413238a57f867c3f

app = Flask(__name__)

@app.route('/')
def index():
    try:
<<<<<<< HEAD
        return render_template('d2_master_board.html')
    except Exception as e:
        return f"Template Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('d2_master_board.html')
    except Exception as e:
        return f"Template Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
        return "Apex Timberline Operations - Service Live and Operational!"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> f23da3a424767cde9e133a6e413238a57f867c3f
