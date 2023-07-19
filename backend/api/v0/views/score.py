from api.v0.views import app_views
from .user.auth import auth_required
from controllers.score import get_scores, get_score
from flask import session, jsonify


@app_views.get("/scores")
@app_views.get("/scores/<score_id>")
@auth_required
def scores_get(score_id=None):
    user_id = session["user_id"]
    if score_id == None:
        scores = get_scores(user_id)
        return jsonify(scores)
    else:
        score = get_score(score_id, user_id)
        if not score:
            return "", 404
        else:
            return jsonify(score), 200
