from datetime import datetime
from scripto import db
from scripto import Script

if __name__ == '__main__':
    db.create_all()
    db.session.add(Script("first_script.sh", True, "old-server", datetime.min))
    db.session.add(Script("db_backup.sh", False, "mysql-server", datetime.today()))
    db.session.add(Script("db_backup.sh", True, "pg-server", datetime.now()))
    db.session.add(Script("last_script.sh", True, "future-server", datetime.max))
    db.session.commit()
