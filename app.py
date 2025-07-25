from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO, join_room, leave_room, emit
from encryption import rsa_utils, aes_utils
import os, json
from cryptography.hazmat.primitives import serialization

app = Flask(__name__)
app.secret_key = os.urandom(24)
socketio = SocketIO(app)

users = {}  # username -> {password, public_key, private_key, rooms}
rooms = {"General": []}  # room_name -> [usernames]
messages = {"General": []}  # room_name -> [messages]

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        encrypted_password = request.form['password']
        password = rsa_utils.decrypt_password(encrypted_password, users[username]['private_key'])
        if users.get(username) and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('chat'))
        return 'Invalid login'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        encrypted_password = request.form['password']
        public_key, private_key = rsa_utils.generate_key_pair()
        password = rsa_utils.decrypt_password(encrypted_password, private_key)
        users[username] = {
            'password': password,
            'public_key': public_key,
            'private_key': private_key,
            'rooms': ['General']
        }
        session['username'] = username
        return redirect(url_for('chat'))
    return render_template('register.html')

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', username=session['username'], rooms=rooms.keys())

@socketio.on('join')
def handle_join(data):
    room = data['room']
    username = session['username']
    join_room(room)
    if username not in rooms[room]:
        rooms[room].append(username)
    emit('message', {'msg': f'{username} has joined {room}'}, room=room)

@socketio.on('send_message')
def handle_message(data):
    room = data['room']
    encrypted_msg = data['msg']
    messages[room].append((session['username'], encrypted_msg))
    emit('message', {'msg': encrypted_msg, 'sender': session['username']}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
