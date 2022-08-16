from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import food
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200


@app.route('/api/food', methods=['GET', 'POST'])
def foods_handler():
    fns = {
        'GET': food.index,
        'POST': food.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


@app.route('/api/food/<int:food_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def food_handler(food_id):
    fns = {
        'GET': food.show,
        'PATCH': food.update,
        'PUT': food.update,
        'DELETE': food.destroy
    }
    resp, code = fns[request.method](request, food_id)
    return jsonify(resp), code


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500


if __name__ == "__main__":
    app.run(debug=True)
