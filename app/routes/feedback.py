from flask import Blueprint, request, jsonify
from ..models import db, Feedback
from ..utils.auth import token_required

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['POST'])
@token_required
def submit_feedback(current_user):
    try:
        data = request.json

        if not data or 'message' not in data:
            return jsonify({"error": "Message is required"}), 400

        feedback = Feedback(user_id=current_user.id, message=data['message'])
        db.session.add(feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Feedback submission failed: {str(e)}"}), 500

@feedback_bp.route('/feedback', methods=['GET'])
@token_required
def get_feedback(current_user):
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403

    try:
        feedbacks = Feedback.query.all()
        result = [
            {"id": f.id, "user_id": f.user_id, "message": f.message}
            for f in feedbacks
        ]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": f"Error retrieving feedback: {str(e)}"}), 500
