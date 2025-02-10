from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/good-home')
def good_home():
    return render_template('good/home.html')
@app.route('/bad-home')
def bad_home():
    return render_template('bad/home_bad.html')


@app.route('/good-design')
def good_design():
    return render_template('good/design.html')
@app.route('/bad-design')
def bad_design():
    return render_template('bad/design_bad.html')


@app.route('/bad-login')
def bad_login():
    return render_template('bad/login_bad.html')
@app.route('/bad-signup')
def bad_signup():
    return render_template('bad/signup_bad.html')


@app.route('/good-login')
def good_login():
    return render_template('good/login.html')
@app.route('/good-signup')
def good_signup():
    return render_template('good/signup.html')


@app.route('/quiz')
def take_quiz():
    return render_template('good/quiz.html')


if __name__ == "__main__":
    app.run(debug=True)
