from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']
    requests.post('http://localhost:5000/users', json={'username': username, 'email': email})
    return redirect(url_for('index'))

@app.route('/get_users', methods=['GET'])
def get_users():
    response = requests.get('http://localhost:5000/users')
    users = response.json()
    return render_template('users.html', users=users)

@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    username = request.form['username']
    email = request.form['email']
    requests.put(f'http://localhost:5000/users/{id}', json={'username': username, 'email': email})
    return redirect(url_for('get_users'))

@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    requests.delete(f'http://localhost:5000/users/{id}')
    return redirect(url_for('get_users'))

if __name__ == '__main__':
    app.run(port=5001)  # Run on port 5001
