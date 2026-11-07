from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return "Apex Timberline Operations - Service Live and Operational!"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
