from flask import g
from flask import Blueprint
from flask import Response
from flask import request

from flask_restful import Api
from flask_restful import Resource

users_bp = Blueprint('users', __name__)
users_api = Api(users_bp)


class UserProfile(Resource):
    def get(self, user_id=None):
        if user_id is None:
            user_id = g.user.user_id

        if user_id is not None:
            args = request.args.to_dict()
            output = {'userInfo': 'userinfo - todo'}
        else:
            output = {'error': True, 'message': 'unknown user'}, 400

        return output


users_api.add_resource(UserProfile, '/users/<string:user_id>')
