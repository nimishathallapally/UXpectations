from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the homepage with good and bad design images
    return render_template('index.html')

@app.route('/good-design')  # Updated URL path for Good Design
def good_design():
    return render_template('design.html')  # Keep current page

@app.route('/bad-design')  # Updated URL path for Bad Design
def bad_design():
    return render_template('design.html')  # Keep current page

if __name__ == "__main__":
    app.run(debug=True)
