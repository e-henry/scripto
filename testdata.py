from datetime import datetime, timedelta
from scripto import db
from scripto import Script

if __name__ == '__main__':
    pastTime=datetime.strptime(datetime.strftime(datetime.utcnow()-timedelta(hours=2), "%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
    futurTime=datetime.strptime(datetime.strftime(datetime.utcnow()+timedelta(hours=2), "%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
    db.create_all()
    db.session.add(Script("late_script.sh", True, "old-server", pastTime, "hourly"))
    db.session.add(Script("failed_backup.sh", False, "mysql-server", datetime.utcnow(), "hourly"))
    db.session.add(Script("ok_backup.sh", True, "pg-server", datetime.utcnow(), "hourly"))
    db.session.add(Script("future_script.sh", True, "future-server", futurTime, "daily"))
    db.session.commit()
