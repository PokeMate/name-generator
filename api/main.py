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


@api.route("/names")
class Names(Resource):
    @api.doc(
        params={
            "amount": "number of generated names: accepted range [1..10], default: 1"
        }
    )
    def get(self):

        # parse the request
        amount = request.args.get("amount")

        # set the default
        if amount == None:
            amount = 1

        # typecast
        try:
            amount = int(amount)
        except (ValueError, TypeError):
            abort(
                400,
                "Bad request: check your query parameter. Expected query string: '.../names?amount=5'",
            )

        if amount > 10 or amount < 1:
            abort(400, "Bad request: amount out of range: accepted range [1..10]")

        # generate the names
        names = generator.generate_names(amount)
        return jsonify(names)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
