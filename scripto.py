"""
Simple flask application to monitor daily script execution
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app = Flask(__name__)

# We'll just use SQLite here so we don't need an external database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scripto.db'

db = SQLAlchemy(app)

class Script(db.Model):
    """A single script"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    status = db.Column(db.Boolean)
    last_exec = db.Column(db.DateTime)

@app.route("/")
def root():
    scripts = Script.query.all()
    return render_template('index.html', scripts=scripts)

if __name__ == '__main__':
    db.create_all()  # make our sqlalchemy tables
    app.run(port=5000, debug=True)
