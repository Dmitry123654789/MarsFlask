from flask import jsonify
from flask_restful import Resource
from .parser_job import parser
from data import db_session
from data.jobs import Jobs


class JobsResource(Resource):
    def get(self, jobs_id):
        session = db_session.create_session()
        jobs = session.get(Jobs, jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader', 'creator'))})

    def delete(self, jobs_id):
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader', 'creator')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            id=args['id'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished'],
            team_leader=args['team_leader'],
            creator=args['creator']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})