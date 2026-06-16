from flask import Flask, request, Response

app = Flask(__name__)

# Mock Database containing user data
users_db = {
    "wiener": {
        "username": "wiener",
        "name": "Peter Wiener",
        "api_key": "wiener_key_abc123"
    },
    "carlos": {
        "username": "carlos",
        "name": "Carlos",
        "api_key": "carlos_secret_api_998877"
    }
}

@app.route('/')
def home():
    return """
    <h2>Welcome to the Account Portal</h2>
    <p>Go to your account: <a href="/myaccount?id=wiener">My Account (wiener)</a></p>
    """

@app.route('/login')
def login():
    return "<h2>Login Page</h2><p>Please log in to access this resource.</p>"

@app.route('/myaccount')
def my_account():
    # Fetching the user ID from the request parameter
    user_id = request.args.get('id')
    
    if user_id in users_db:
        user_data = users_db[user_id]
        
        # HTML Content that contains sensitive user data
        leak_content = f"""<html>
        <head><title>Account Details</title></head>
        <body>
            <h1>Welcome back, {user_data['name']}</h1>
            <p>Username: {user_data['username']}</p>
            <p>Your Confidential API Key: <strong>{user_data['api_key']}</strong></p>
        </body>
        </html>"""
        
        # The application attempts to enforce access control by redirecting unauthorized requests,
        # but it handles the HTTP response headers and body in a flawed manner.
        headers = {'Location': '/login'}
        return Response(leak_content, status=302, headers=headers)
        
    return "User not found", 404

if __name__ == '__main__':
    print("Starting lab server on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
