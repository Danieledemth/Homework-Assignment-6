from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Define the file path for storing user profiles
user_data_file = 'user_data.txt'

# Helper function to read user data from the file
def read_user_data():
    if os.path.exists(user_data_file):
        with open(user_data_file, 'r') as f:
            return json.load(f)
    return {}

# Helper function to write user data to the file
def write_user_data(data):
    with open(user_data_file, 'w') as f:
        json.dump(data, f, indent=4)

# User Registration Endpoint (POST /add_user)
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if 'email' not in data or 'age' not in data:
        return jsonify({"error": "Missing email or age"}), 400

    email = data['email']
    age = data['age']

    # Get existing user data
    users = read_user_data()

    # Check if user already exists
    if email in users:
        return jsonify({"error": "User already exists"}), 400

    # Add new user
    users[email] = {'email': email, 'age': age}

    # Write updated user data back to file
    write_user_data(users)

    return jsonify({"message": "User added successfully"}), 201

# Retrieve user profile (GET /get_user/<email>)
@app.route('/get_user/<email>', methods=['GET'])
def get_user(email):
    users = read_user_data()

    if email in users:
        return jsonify(users[email])
    else:
        return jsonify({"error": "User not found"}), 404

# Update user profile (PUT /update_user/<email>)
@app.route('/update_user/<email>', methods=['PUT'])
def update_user(email):
    data = request.get_json()
    users = read_user_data()

    if email not in users:
        return jsonify({"error": "User not found"}), 404

    # Update user information
    if 'age' in data:
        users[email]['age'] = data['age']
    
    write_user_data(users)

    return jsonify({"message": "User updated successfully"}), 200

# Delete user profile (DELETE /delete_user/<email>)
@app.route('/delete_user/<email>', methods=['DELETE'])
def delete_user(email):
    users = read_user_data()

    if email in users:
        del users[email]
        write_user_data(users)
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)  