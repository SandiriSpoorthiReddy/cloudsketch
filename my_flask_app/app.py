from flask import Flask, render_template, request, redirect, url_for, flash, session
import subprocess
import os

app = Flask(__name__)

# Securely generate a secret key for session management
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24)  # Random key to ensure secure sessions

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        
        # Validate username and password (simplified for this example)
        if username == 'user' and password == 'pass':
            session['logged_in'] = True  # Set session status
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/index')
def index():
    if not session.get('logged_in'):  # Check if user is logged in
        flash("Please log in first.")
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/run_hand_detection')
def run_hand_detection():
    if not session.get('logged_in'):  # Ensure user is logged in
        flash("Please log in first.")
        return redirect(url_for('home'))
    
    try:
        # Run HandDetection.py and capture output
        result = subprocess.run(['python', 'HandDetection.py'], check=True, capture_output=True, text=True)
        flash('Hand detection script ran successfully: {result.stdout}')
        return redirect(url_for('index'))
    except subprocess.CalledProcessError as e:
        flash(f'Error running hand detection: {e.stderr}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
