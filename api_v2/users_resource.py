import datetime

from flask import jsonify
from flask_restful import Resource, abort
from .parser_user import parser
from data import db_session
from data.users import User


class UsersResource(Resource):
    def get(self, users_id):
        session = db_session.create_session()
        users = session.get(User, users_id)
        if not users:
            abort(404)
        return jsonify({'users': users.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date', 'city_from'))})

    def delete(self, users_id):
        session = db_session.create_session()
        users = session.get(User, users_id)
        if not users:
            abort(404)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})

class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date', 'city_from')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            modified_date=datetime.datetime.strptime(args['modified_date'], '%Y-%m-%d %H:%M:%S'),
            city_from=args['city_from']
        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})