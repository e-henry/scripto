"""
Simple flask application to monitor daily script execution
"""

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager


app = Flask(__name__)

# We'll just use SQLite here so we don't need an external database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../scripto.db'

db = SQLAlchemy(app)
# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)


class Script(db.Model):
    """A single script"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    status = db.Column(db.Boolean)
    server = db.Column(db.String())
    last_exec = db.Column(db.DateTime)

    def __init__(self, name, status, server, last_exec):
        self.name = name
        self.status = status
        self.server = server
        self.last_exec = last_exec

    def __repr__(self):
        return '<Script %r>' % self.name


@app.route("/")
def root():
    scripts = Script.query.order_by("status").order_by("last_exec").all()
    return render_template('index.html', scripts=scripts)


# Rest api for script table
manager.create_api(Script, url_prefix="/api/v1",
                   methods=['GET', 'POST', 'PUT', 'DELETE'])


if __name__ == '__main__':
    db.create_all()  # make our sqlalchemy tabless
    app.run(port=5000, debug=True)
