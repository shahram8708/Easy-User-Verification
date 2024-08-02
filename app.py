from flask import Flask, request, jsonify, redirect, url_for, session, render_template
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash
from functools import wraps
import random
import string

app = Flask(__name__)
app.secret_key = 'supersecretkey'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ram.coding8@gmail.com'  
app.config['MAIL_PASSWORD'] = 'lkbf nrwm pmno xqdh'  
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

users = {}
verification_codes = {}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('verify'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if email in users:
        return jsonify({'success': False, 'message': 'User already exists'})

    hashed_password = generate_password_hash(password)
    users[email] = {'username': username, 'password': hashed_password}
    
    verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    verification_codes[email] = verification_code

    msg = Message('Email Verification', sender='ram.coding8@gmail.com', recipients=[email])
    msg.body = f'Hello {username},\n\nPlease verify your email address by clicking the link below:\n\nhttps://easy-user-verification.onrender.com/verify_email/{verification_code}\n\nThank you!'
    mail.send(msg)

    return jsonify({'success': True})

@app.route('/verify_email/<code>', methods=['GET'])
def verify_email(code):
    for email, verification_code in verification_codes.items():
        if verification_code == code:
            session['email'] = email
            del verification_codes[email]
            return redirect(url_for('dashboard'))
    return 'Invalid or expired verification code', 400

@app.route('/check_verification', methods=['GET'])
def check_verification():
    if 'email' in session:
        return jsonify({'verified': True})
    return jsonify({'verified': False})

@app.route('/dashboard')
@login_required
def dashboard():
    email = session.get('email')
    user = users.get(email)
    if user:
        return render_template('dashboard.html', username=user["username"], email=email)
    return 'User not found', 404

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('email', None)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
