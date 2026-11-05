import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 25px; min-height: 90vh;">
        <div style="border: 2px solid #0f0; padding: 15px; background: #111; margin-bottom: 20px;">
            <h2 style="margin: 0; color: #0f0;">[D2 / D3 / D5: AUTHENTICATED MEMBER BOARDS]</h2>
            <p style="margin: 5px 0 0 0; color: #ff0;"><b>Status:</b> Active Subscriber Access & Database Sync Enabled</p>
        </div>
        <h3>Member Modules Active:</h3>
        <ul style="line-height: 1.8;">
            <li><b>D2 Member:</b> Full Spatial Lead Search & Territory Claims</li>
            <li><b>D3 Member:</b> Live Field Terminal & Dispatch Queue</li>
            <li><b>D5 Member:</b> Active Estimator, Contract Writer & Neighbor Scan [$1.50]</li>
        </ul>
    </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
