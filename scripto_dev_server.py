from scripto import app
from scripto import db


if __name__ == '__main__':
    db.create_all()  # make our sqlalchemy tabless
    app.run(port=5000, debug=True)
