from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = '123'

# dựng website đơn giản, bao gồm các trang:
# -   Trang home giới thiệu
# -   Trang Đăng nhập
# -   Trang Đăng ký
# -   Không cần sử dụng Database

users_file = "user.json"

def load_users():
    try:
        with open(users_file, 'r') as file:
            return json.load(file)
    except:
        return {}
    
def save_user(user : dict):
    data = load_users()
    data[len(data)+1] = user
    with open(users_file, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def home():
    if session.get('isLogin'):
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

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
            save_user(new_user)
            success_message = "Registration successful!"

    return render_template('register.html', error=error, success_message=success_message)

def is_valid_user_register(user : dict):
    users = load_users()

    for idx in users:
        if(users[idx]['username'] == user['username']):
            return "Username already exists"
        if(users[idx]['email'] == user['email']):
            return "Email already exists"
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = is_valid_user_login(username, password)
            
        if(error == None):
            session['isLogin'] = True
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

def is_valid_user_login(username : str, password : str):
    users = load_users()

    for idx in users:
        if(users[idx]['username'] == username):
            if(users[idx]['password'] == password):
                return None
            
    return "Invalid username or password"

@app.route('/logout')
def logout():
    session.pop('isLogin', None)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

