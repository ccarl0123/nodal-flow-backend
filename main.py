from flask import Flask, jsonify, request
from flask_cors import CORS
import os
# Create our robot app
app = Flask(__name__)
CORS(app) # Let our website talk to our robot
# Home page - says hello
@app.route('/')
def home():
return jsonify({
"message": " NODAL FLOW Backend is alive!",
"app": "Spiritual-Tech API",
"status": "running"
})
# Health check - is our robot working?
@app.route('/api/health')
def health():
return jsonify({
"service": "nodal-flow-backend",
"status": "healthy",
"message": "Robot is working perfectly! "
})
# Register a new user
@app.route('/api/auth/register', methods=['POST'])
def register():
data = request.get_json()
return jsonify({
"message": "Welcome to NODAL FLOW! ",
"user": {
"name": f"{data.get('firstName', 'Spiritual')}
{data.get('lastName', 'Seeker')}",
"email": data.get('email', 'user@nodalflow.com'),
"id": 1
},
"token": "magic_token_123"
})
# Login user
@app.route('/api/auth/login', methods=['POST'])
def login():
data = request.get_json()
return jsonify({
"message": "Welcome back! ",
"user": {
"name": "Spiritual Seeker",
"email": data.get('email', 'user@nodalflow.com'),
"id": 1
},
"token": "magic_token_123"
})
# Calculate life path number (simple numerology)
@app.route('/api/calculate/life-path', methods=['POST'])
def calculate_life_path():
data = request.get_json()
birth_date = data.get('birthDate', '1990-01-01')
# Simple calculation: add all digits in birth date
numbers = [int(d) for d in birth_date if d.isdigit()]
total = sum(numbers)
# Reduce to single digit
while total > 9:
total = sum(int(d) for d in str(total))
return jsonify({
"lifePath": total,
"meaning": f"Your Life Path {total} means you are
destined for greatness! ",
"guidance": "Follow your heart and trust your intuition
today."
})
# Voice personalities
@app.route('/api/voice/personalities')
def voice_personalities():
return jsonify({
"message": "Voice guidance powered by your browser -
FREE! ",
"voices": {
"sage": {
"name": "Sage Wisdom",
"description": "Calm and wise voice for
guidance",
"icon": " "
},
"mystic": {
"name": "Mystic Oracle",
"description": "Ethereal voice for spiritual
insights",
"icon": " "
}
}
})
# Subscription plans
@app.route('/api/payment/plans')
def payment_plans():
return jsonify({
"plans": [
{
"name": "Free",
"price": 0,
"features": ["Basic life path calculation",
"Daily guidance"]
},
{
"name": "Silver",
"price": 9.99,
"features": ["Full numerology", "Voice
guidance", "Compatibility"]
},
{
"name": "Gold",
"price": 14.99,
"features": ["Advanced astrology", "Custom
readings", "Priority support"]
}
]
})
# Daily guidance
@app.route('/api/guidance/daily/<user_id>')
def daily_guidance(user_id):
import random
guidance_messages = [
"Today is perfect for new beginnings! ",
"Trust your intuition - it's guiding you well ",
"Focus on gratitude and watch magic happen ",
"Your spiritual energy is particularly strong today ",
"Listen to your heart - it knows the way "
]
return jsonify({
"date": "2025-06-19",
"message": random.choice(guidance_messages),
"energy": "High ",
"focus": "Spiritual growth and inner wisdom"
})
# Start our robot!
if __name__ == '__main__':
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)
