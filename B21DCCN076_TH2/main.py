from flask import Flask, render_template, request, redirect, url_for, session
import csv
import time

app = Flask(__name__)
app.secret_key = '123'

DB_FILE = "DB.csv"
FB_FILE = "feedback.csv"

def load_users():
    try:
        with open(DB_FILE, 'r') as file:
            data = csv.reader(file, delimiter=';')
            users = []
            for row in data:
                if row:
                    username, password, email = row
                    user = {
                        'username': username,
                        'password': password,
                        'email': email
                    }
                    users.append(user)
            return users
    except FileNotFoundError:
        return []

def save_users(users):
    with open(DB_FILE, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for user in users:
            writer.writerow([user['username'], user['password'], user['email']])

def load_feedback():
    try:
        with open(FB_FILE, 'r') as file:
            data = csv.reader(file, delimiter=';')
            feedbacks = []
            for row in data:
                if row:
                    username, feedback, time = row
                    feedback = {
                        'username': username,
                        'feedback': feedback,
                        'time': time
                    }
                    feedbacks.append(feedback)
            return feedbacks
    except FileNotFoundError:
        return []

def save_feedback(feedbacks):
    with open(FB_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for feedback in feedbacks:
            writer.writerow([feedback['username'], feedback['feedback'], feedback['time']])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success_message = None

    if request.method == 'POST':
        new_user = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': request.form['password']
        }

        error = is_valid_user_register(new_user)

        if error is None:
            users = load_users()
            users.append(new_user)
            save_users(users)
            success_message = "Registration successful!"

    return render_template('register.html', error=error, success_message=success_message)


def is_valid_user_register(user):
    users = load_users()

    for existing_user in users:
        if existing_user['username'] == user['username']:
            return "Account already exists"

    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = is_valid_user_login(username, password)

        if error is None:
            session['isLogin'] = True
            session['username'] = username
            return redirect(url_for('home'))

    return render_template('login.html', error=error)

def is_valid_user_login(username, password):
    users = load_users()

    for user in users:
        if user['username'] == username and user['password'] == password:
            return None

    return "Invalid username or password"

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if 'isLogin' not in session or not session['isLogin']:
        return redirect(url_for('login'))

    if request.method == 'POST':
        username = session['isLogin']
        user_feedback = request.form['feedback']
        current_time = time.strftime("%S:%M:%H %d/%m/%Y")
        feedback_entry = {
            'username': username,
            'feedback': user_feedback,
            'time': current_time
        }
        feedbacks = load_feedback()
        feedbacks.append(feedback_entry)
        save_feedback(feedbacks)

    return render_template('feedback.html')

@app.route('/logout')
def logout():
    session.pop('isLogin', None)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
