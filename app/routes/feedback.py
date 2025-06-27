from flask import Blueprint, request, jsonify
from ..models import db, Feedback

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.json
        if not all(k in data for k in ('user_id', 'message')):
            return jsonify({"error": "Missing user_id or message"}), 400

        feedback = Feedback(user_id=data['user_id'], message=data['message'])
        db.session.add(feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Feedback submission failed: {str(e)}"}), 500

@feedback_bp.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        feedbacks = Feedback.query.all()
        result = [{"id": f.id, "user_id": f.user_id, "message": f.message} for f in feedbacks]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving feedback: {str(e)}"}), 500
