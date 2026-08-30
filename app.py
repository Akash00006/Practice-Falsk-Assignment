from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the App'

 
@app.route('/health')
def health():
    return 'App is running'


# Task 3: In-memory dictionary to store username and password pairs
passwords_db = {}
#,,,,,
# Endpoint 1: Save credentials using POST
@app.route('/add', methods=['POST'])
def add_password():
    data = request.get_json()
    
    # Check if request contains valid JSON and required fields
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing 'username' or 'password' in request body"}), 400
    
    username = data['username']
    password = data['password']
    
    # Store credentials in memory
    passwords_db[username] = password
    return jsonify({"message": f"Password saved successfully for '{username}'"}), 201

# Endpoint 2: Retrieve stored password by username using GET
@app.route('/get/<username>', methods=['GET'])
def get_password(username):
    # Search for username in dictionary
    if username in passwords_db:
        return jsonify({"username": username, "password": passwords_db[username]}), 200
    
    # Handle user not found case
    return jsonify({"error": "Username not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)