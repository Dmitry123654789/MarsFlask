import datetime

from flask import jsonify, make_response
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
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date',
                  'city_from'))})

    def delete(self, users_id):
        session = db_session.create_session()
        users = session.get(User, users_id)
        if not users:
            abort(404)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, users_id):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        user = db_sess.get(User, users_id)
        if not user:
            return make_response(jsonify({'error': 'Not found'}), 404)

        elif all(key in args for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
                  'modified_date']) and len(args) == 9:
            for key, value in args.items():
                if key == 'modified_date':
                    setattr(user, key, datetime.datetime.strptime(args['modified_date'], '%Y-%m-%d %H:%M:%S'))
                else:
                    setattr(user, key, value)
            db_sess.commit()
            return jsonify({'success': 'OK'})

        return make_response(jsonify({'error': 'Bad request'}), 400)


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=(
            'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date', 'city_from'))
            for item in users]})

    def post(self):
        args = parser.parse_args()
        if not args:
            return make_response(jsonify({'error': 'Empty request'}), 400)
        elif all(key in args for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
                  'modified_date']) and len(args) == 9:
            db_sess = db_session.create_session()
            users = User(
                surname=args['surname'],
                name=args['name'],
                age=args['age'],
                position=args['position'],
                speciality=args['speciality'],
                address=args['address'],
                email=args['email'],
                city_from=args['city_from'],
                modified_date=datetime.datetime.strptime(args['modified_date'], '%Y-%m-%d %H:%M:%S')
            )
            db_sess.add(users)
            db_sess.commit()
            return jsonify({'id': users.id})

        return make_response(jsonify({'error': 'Bad request'}), 400)
