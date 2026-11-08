from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('d2_master_board.html')
    except Exception as e:
        return f"Template Error: {str(e)}", 500

@app.route('/d2')
def d2_master_board():
    try:
        return render_template('d2_master_board.html')
    except Exception as e:
        return f"D2 Template Error: {str(e)}", 500

@app.route('/d4')
def d4_outreach():
    return jsonify({
        "service": "apex-timberline-d4-outreach",
        "status": "active",
        "timeblocks": ["10:00 AM - 12:00 PM", "2:00 PM - 4:00 PM"],
        "budget_cap": "$25-$30 monthly"
    })

@app.route('/d5', methods=['GET', 'POST'])
def d5_hazard_scan():
    scan_status = None
    selected_tier = None
    if request.method == 'POST':
        selected_tier = request.form.get('scan_tier', 'standard')
        scan_status = f"Completed ({selected_tier.capitalize()} Tier)"
    
    return render_template('d5_hazard_scan.html', scan_status=scan_status, selected_tier=selected_tier)

@app.route('/d6')
def d6_admin():
    return jsonify({
        "service": "apex-timberline-d6-admin",
        "status": "governance_active",
        "governance": "Master Governance & System Logging"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)