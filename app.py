from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory list to store user data
users = []

# User ID counter
user_id_counter = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    if not request.json or 'name' not in request.json:
        abort(400)
    
    user = {
        'id': user_id_counter,
        'name': request.json['name'],
        'email': request.json.get('email', "")
    }
    users.append(user)
    user_id_counter += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404)
    
    if not request.json:
        abort(400)

    user['name'] = request.json.get('name', user['name'])
    user['email'] = request.json.get('email', user['email'])
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
