from flask import Blueprint, request, jsonify
from ..models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not all(k in data for k in ('username', 'email', 'password')):
            return jsonify({"error": "Missing required fields"}), 400

        if User.query.filter_by(email=data['email']).first():
            return jsonify({"error": "Email already registered"}), 409

        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Registration failed: {str(e)}"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not all(k in data for k in ('email', 'password')):
            return jsonify({"error": "Missing email or password"}), 400

        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": f"Login failed: {str(e)}"}), 500
