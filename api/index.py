from flask import Flask, request, jsonify
from flask_cors import CORS
import werkzeug.security as security

app = Flask(__name__)
CORS(app)

# Institutional DB for Aravali College
users_db = {
    "admin@aravali.edu": security.generate_password_hash("acem_admin_2026"),
    "electrician@aravali.edu": security.generate_password_hash("guard_99")
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email in users_db and security.check_password_hash(users_db[email], password):
        role = 'admin' if 'admin' in email else 'staff'
        return jsonify({"status": "success", "role": role, "token": "SECURE_VGUARD_TOKEN"}), 200
    
    return jsonify({"status": "error", "message": "Invalid Credentials"}), 401

# Vercel needs this to handle the app
def handler(event, context):
    return app(event, context)
