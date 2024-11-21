from flask import Flask, render_template, request, redirect, url_for, flash, session
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key

@app.route('/')
def home():
    return render_template('login.html')  # Renders the HTML form

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email')  # Updated form field names
    password = request.form.get('password')

    # Mocked validation for simplicity
    if username == 'user@gmail.com' and password == 'pass':
        session['logged_in'] = True
        return redirect(url_for('index'))
    else:
        flash("Invalid username or password")
        return redirect(url_for('home'))

@app.route('/index')
def index():
    if not session.get('logged_in'):  # Ensure the user is logged in
        flash("Please log in first.")
        return redirect(url_for('home'))
    return render_template('index.html')  # Create an `index.html` template

@app.route('/run_hand_detection')
def run_hand_detection():
    if not session.get('logged_in'):
        flash("Please log in first.")
        return redirect(url_for('home'))

    try:
        # Run the HandDetection.py script
        result = subprocess.run(['python', 'HandDetection.py'], check=True, capture_output=True, text=True)
        flash('Hand detection script ran successfully.')
        return redirect(url_for('index'))
    except subprocess.CalledProcessError as e:
        flash(f'Error running hand detection: {e.stderr}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
