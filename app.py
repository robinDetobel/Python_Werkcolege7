from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def show_home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

@app.route('/friends')
def show_friends():
    return render_template("friends.html", vriendjes=["Robin Detobel", "Aäron Staes", "Bernard Soumi", "David van Steertegem", "Davy van Belle"])

@app.route('/someke')
def show_som():
    return render_template("som.html")
