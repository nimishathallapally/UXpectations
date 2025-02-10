from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/good-design')
def good_design():
    return render_template('good/design.html')

@app.route('/bad-design')
def bad_design():
    return render_template('bad/home_bad.html')

@app.route('/login')
def login():
    return render_template('good/login.html')

@app.route('/signup')
def signup():
    return render_template('good/signup.html')

@app.route('/quiz')
def take_quiz():
    return render_template('good/quiz.html')

if __name__ == "__main__":
    app.run(debug=True)
