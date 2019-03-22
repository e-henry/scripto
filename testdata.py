from datetime import datetime, timedelta
from scripto import db
from scripto import Script

if __name__ == '__main__':
    pastTime=datetime.strptime(datetime.strftime(datetime.now()-timedelta(hours=2), "%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
    futurTime=datetime.strptime(datetime.strftime(datetime.now()+timedelta(hours=2), "%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
    db.create_all()
    db.session.add(Script("first_script.sh", True, "old-server", pastTime, "hourly"))
    db.session.add(Script("db_backup.sh", False, "mysql-server", datetime.today(), "hourly"))
    db.session.add(Script("db_backup.sh", True, "pg-server", datetime.now(), "hourly"))
    db.session.add(Script("last_script.sh", True, "future-server", futurTime, "daily"))
    db.session.commit()
