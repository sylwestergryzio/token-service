from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class TokenService(Resource):
    def get(self):
        token = request.headers.get('X-Forwarded-Access-Token')
        return {
            'message': 'OK',
            'token': token
            }

api.add_resource(TokenService, '/')

if __name__ == "__main__":
    app.run(debug=True) 