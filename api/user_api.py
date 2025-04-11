import datetime

import flask
from flask import jsonify, make_response, request
from data import db_session
from data.users import User

blueprint = flask.Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=(
                    'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
                    'modified_date')) for item in users]
        }
    )


@blueprint.route('/users/<users_id>', methods=['GET'])
def get_one_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.get(User, users_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'users': users.to_dict(only=(
                'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
                'modified_date'))
        }
    )


@blueprint.route('/users', methods=['POST'])
def create_users():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif all(key in request.json for key in
             ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
              'modified_date']) and len(request.json) == 9:
        db_sess = db_session.create_session()
        users = User(
            surname=request.json['surname'],
            name=request.json['name'],
            age=request.json['age'],
            position=request.json['position'],
            speciality=request.json['speciality'],
            address=request.json['address'],
            email=request.json['email'],
            city_from=request.json['city_from'],
            modified_date=datetime.datetime.strptime(request.json['modified_date'], '%Y-%m-%d %H:%M:%S')
        )
        db_sess.add(users)
        db_sess.commit()
        return jsonify({'id': users.id})

    return make_response(jsonify({'error': 'Bad request'}), 400)


@blueprint.route('/users/<users_id>', methods=['DELETE'])
def delete_users(users_id):
    db_sess = db_session.create_session()
    users = db_sess.get(User, users_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/users/<users_id>', methods=['PUT'])
def update_users(users_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, users_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)

    elif all(key in request.json for key in
             ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from',
              'modified_date']) and len(request.json) == 9:
        for key, value in request.json.items():
            if key == 'modified_date':
                setattr(user, key, datetime.datetime.strptime(request.json['modified_date'], '%Y-%m-%d %H:%M:%S'))
            else:
                setattr(user, key, value)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    return make_response(jsonify({'error': 'Bad request'}), 400)

