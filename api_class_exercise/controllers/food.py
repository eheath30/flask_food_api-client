''' Food controller '''
from werkzeug.exceptions import BadRequest

foods = [
    {'id': 1, 'name': 'Fish and chips'},
    {'id': 2, 'name': 'Spaghetti Bolognese'},
    {'id': 3, 'name': 'Mac and Cheese'},
    {'id': 4, 'name': 'Chicken Nuggets'}
]


def index(req):
    return [f for f in foods], 200


def show(req, uid):
    return find_by_uid(uid), 200


def create(req):
    new_food = req.get_json()
    # creates new id
    new_food['id'] = sorted([f['id'] for f in foods])[-1] + 1
    foods.append(new_food)
    return new_food, 201


def update(req, uid):
    food = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        food[key] = val
    return food, 200


def destroy(req, uid):
    food = find_by_uid(uid)
    foods.remove(food)
    return food, 204


def find_by_uid(uid):
    try:
        return next(dish for dish in foods if dish['id'] == uid)
    except:
        raise BadRequest(f"We don't have that food with id {uid}!")
