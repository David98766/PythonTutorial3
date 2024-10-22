from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Landing Page Route
@app.route('/')
def landing_page():
    return render_template('LandingPage.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # For now, redirect to the products page after login (without validation)
        return redirect(url_for('product_spread'))
    return render_template('login.html')

# Product Spread Route
@app.route('/products')
def product_spread():
    return render_template('ProductSpread.html')

if __name__ == '__main__':
    app.run(debug=True)

