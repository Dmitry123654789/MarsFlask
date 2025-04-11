import datetime

import flask
from flask import jsonify, make_response, request
from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    'id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader',
                    'creator', 'hazard_category_id')) for item in jobs]
        }
    )


@blueprint.route('/jobs/<jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader',
                'creator', 'hazard_category_id'))
        }
    )


@blueprint.route('/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif all(key in request.json for key in
             ['job', 'work_size', 'collaborators', 'is_finished', 'start_date', 'team_leader', 'creator',
              'end_date', 'is_finished', 'hazard_category_id']) and len(request.json) == 9:
        db_sess = db_session.create_session()
        jobs = Jobs(
            job=request.json['job'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            start_date=datetime.datetime.strptime(request.json['start_date'], '%Y-%m-%d %H:%M:%S'),
            end_date=datetime.datetime.strptime(request.json['end_date'], '%Y-%m-%d %H:%M:%S'),
            is_finished=request.json['is_finished'],
            team_leader=request.json['team_leader'],
            creator=request.json['creator'],
            hazard_category_id=request.json['hazard_category_id']
        )
        db_sess.add(jobs)
        db_sess.commit()
        return jsonify({'id': jobs.id})

    return make_response(jsonify({'error': 'Bad request'}), 400)

@blueprint.route('/jobs/<jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})

@blueprint.route('/jobs/<jobs_id>', methods=['PUT'])
def update_jobs(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.get(Jobs, jobs_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    elif len(request.json) == 9 and all(key in request.json for key in
             ['job', 'work_size', 'collaborators', 'is_finished', 'start_date', 'team_leader', 'creator',
              'end_date', 'is_finished', 'hazard_category_id']):
        for key, value in request.json.items():
            if key in ['end_date', 'start_date']:
                setattr(job, key, datetime.datetime.strptime(request.json[key], '%Y-%m-%d %H:%M:%S'))
            else:
                setattr(job, key, value)

        db_sess.commit()
        return jsonify({'success': 'OK'})
    return make_response(jsonify({'error': 'Bad request'}), 400)