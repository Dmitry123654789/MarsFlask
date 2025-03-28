import flask
from flask import jsonify, make_response

from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/jobs', methods=['GET'])
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    'id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader',
                    'creator')) for item in jobs]
        }
    )


@blueprint.route('/jobs/<news_id>', methods=['GET'])
def get_one_news(news_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(news_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader',
                'creator'))
        }
    )
