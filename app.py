from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about-us")
def about():
	return render_template('index.html')

@app.route("/CS4800")
def CS4800():
    return "Welcome CS4800 to our CPP Map Finder application!"

if __name__ == "__main__":
    app.run(debug=True)
