from flask import Flask, escape, request, jsonify, abort
from flask_restplus import Api, Resource, reqparse
from generator import NameGenerator

import os

# flask app configuration
app = Flask(__name__)
api = Api(app, doc="/swagger/")

# generator configuration
model_path = os.path.realpath("./api/static//model.h5")
input_names_path = os.path.realpath("./api/static/names.txt")
generator = NameGenerator(model_path, input_names_path)


# routes
@api.route("/home")
class Home(Resource):
    @api.doc("home")
    def get(self):
        return jsonify("Welcome to PokeMate random name generator!")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
