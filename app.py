import flask
from flask import Flask, render_template

app = flask.Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return flask.render_template("templates/index.html")


@app.route('/about')
def about():
    return flask.render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + "-" + str(id)


if __name__ == "__main__":
    app.run(debug=True)