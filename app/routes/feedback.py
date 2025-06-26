from flask import Blueprint, request, jsonify
from ..models import db, Feedback

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    feedback = Feedback(user_id=data['user_id'], message=data['message'])
    db.session.add(feedback)
    db.session.commit()
    return jsonify({"message": "Feedback submitted successfully"})

@feedback_bp.route('/feedback', methods=['GET'])
def get_feedback():
    feedbacks = Feedback.query.all()
    return jsonify([{"id": f.id, "user_id": f.user_id, "message": f.message} for f in feedbacks])
