from flask import Flask, escape, request, jsonify, abort
from flask_restplus import Api, Resource, reqparse

import os

# flask app configuration
app = Flask(__name__)
api = Api(app, doc="/swagger/")

# routes
@api.route('/home')
class Home(Resource):
    @api.doc('home')
    def get(self):
        return jsonify("Welcome to PokeMate random name generator!")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
