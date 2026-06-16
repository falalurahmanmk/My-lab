from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Mock database
products = [
    {"id": 1, "name": "Cyber Security Hoodie", "price": "$49.99", "image": "👕"},
    {"id": 2, "name": "Hacker Mechanical Keyboard", "price": "$89.99", "image": "⌨️"},
    {"id": 3, "name": "Premium VPN 1-Year", "price": "$29.99", "image": "🌐"}
]

# Real-looking HTML/CSS Interface
BASE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SecShop - Premium Hacker Gear</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; margin: 0; padding: 0; }
        header { background-color: #1e293b; color: white; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; }
        header h1 { margin: 0; font-size: 24px; color: #38bdf8; }
        nav a { color: #cbd5e1; text-decoration: none; margin-left: 20px; font-weight: 500; }
        nav a:hover { color: white; }
        .container { max-width: 1100px; margin: 40px auto; padding: 0 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; }
        .card { background: white; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); padding: 20px; text-align: center; }
        .card .icon { font-size: 50px; margin-bottom: 10px; }
        .card h3 { margin: 10px 0; color: #1e293b; }
        .card .price { color: #0ea5e9; font-weight: bold; font-size: 18px; margin-bottom: 15px; }
        .btn { background-color: #1e293b; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; display: inline-block; }
        .btn:hover { background-color: #334155; }
        footer { text-align: center; padding: 20px; color: #64748b; font-size: 14px; margin-top: 50px; }
        .admin-box { background: #fee2e2; border: 1px solid #f87171; border-radius: 8px; padding: 20px; color: #991b1b; }
    </style>
</head>
<body>
    <header>
        <h1>🔒 SecShop</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/myaccount">My Account</a>
        </nav>
    </header>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <footer>© 2026 SecShop Inc. Built for Security Training.</footer>
</body>
</html>
"""

@app.route('/')
def home():
    home_template = """
    {% extends "base" %}
    {% block content %}
    <h2>Featured Products</h2>
    <p>Welcome to the ultimate store for cybersecurity professionals.</p>
    <div class="grid">
        {% for p in products %}
        <div class="card">
            <div class="icon">{{ p.image }}</div>
            <h3>{{ p.name }}</h3>
            <div class="price">{{ p.price }}</div>
            <button class="btn">Buy Now</button>
        </div>
        {% endfor %}
    </div>
    {% endblock %}
    """
    return render_template_string(BASE_TEMPLATE + home_template, products=products)

@app.route('/myaccount')
def my_account():
    # A standard user account page simulation
    account_template = """
    {% extends "base" %}
    {% block content %}
    <h2>User Account Portal</h2>
    <div class="card" style="text-align: left; max-width: 500px;">
        <p><strong>Username:</strong> guest_user</p>
        <p><strong>Role:</strong> Standard Customer</p>
        <p><strong>Email:</strong> guest@secshop.local</p>
    </div>
    {% endblock %}
    """
    return render_template_string(BASE_TEMPLATE + account_template)

# --- VULNERABLE AREA BELOW (No clues detailed!) ---

@app.route('/admin-panel')
def admin_panel():
    admin_template = """
    {% extends "base" %}
    {% block content %}
    <div class="admin-box">
        <h2>⚠️ Unauthorized Admin Console</h2>
        <p>Welcome to the sensitive management area.</p>
        <hr style="border: 0; border-top: 1px solid #f87171;">
        <p><strong>CRITICAL FLAG:</strong> <span style="background: yellow; padding: 5px; font-family: monospace;">SS_ACCESS_KEY_SECRET_771122</span></p>
    </div>
    {% endblock %}
    """
    return render_template_string(BASE_TEMPLATE + admin_template)

@app.before_request
def check_access():
    if request.path == '/admin-panel':
        # The application tries to prevent standard users from accessing the admin panel
        # by checking a specific aspect of the request context, but the logic is flawed.
        user_role = request.headers.get('X-Custom-User-Role', 'Guest')
        is_admin_route = request.args.get('admin', 'false')
        
        if user_role != 'Administrator' and is_admin_route != 'true':
            return redirect('/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
