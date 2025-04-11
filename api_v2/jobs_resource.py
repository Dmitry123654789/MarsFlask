import datetime

from flask import jsonify, make_response
from flask_restful import Resource, abort
from .parser_job import parser
from data import db_session
from data.jobs import Jobs


class JobsResource(Resource):
    def get(self, jobs_id):
        session = db_session.create_session()
        jobs = session.get(Jobs, jobs_id)
        if not jobs:
            abort(404)
        return jsonify({'jobs': jobs.to_dict(
            only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader', 'creator', 'hazard_category_id'))})

    def delete(self, jobs_id):
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        if not jobs:
            abort(404)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, jobs_id):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job = db_sess.get(Jobs, jobs_id)
        if not job:
            return make_response(jsonify({'error': 'Not found'}), 404)
        elif len(args) == 9 and all(key in args for key in
                                            ['job', 'work_size', 'collaborators', 'is_finished', 'start_date',
                                             'team_leader', 'creator',
                                             'end_date', 'is_finished', 'hazard_category_id']):
            for key, value in args.items():
                if key in ['end_date', 'start_date']:
                    setattr(job, key, datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S'))
                else:
                    setattr(job, key, value)

            db_sess.commit()
            return jsonify({'success': 'OK'})
        return make_response(jsonify({'error': 'Bad request'}), 400)

class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader', 'creator', 'hazard_category_id')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        if not args:
            return make_response(jsonify({'error': 'Empty request'}), 400)
        elif all(key in args for key in
                 ['job', 'work_size', 'collaborators', 'is_finished', 'start_date', 'team_leader', 'creator',
                  'end_date', 'is_finished', 'hazard_category_id']) and len(args) == 9:
            db_sess = db_session.create_session()
            jobs = Jobs(
                job=args['job'],
                work_size=args['work_size'],
                collaborators=args['collaborators'],
                start_date=datetime.datetime.strptime(args['start_date'], '%Y-%m-%d %H:%M:%S'),
                end_date=datetime.datetime.strptime(args['end_date'], '%Y-%m-%d %H:%M:%S'),
                is_finished=args['is_finished'],
                team_leader=args['team_leader'],
                creator=args['creator'],
                hazard_category_id=args['hazard_category_id']
            )
            db_sess.add(jobs)
            db_sess.commit()
            return jsonify({'id': jobs.id})

        return make_response(jsonify({'error': 'Bad request'}), 400)