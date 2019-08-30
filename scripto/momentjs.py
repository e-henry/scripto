from jinja2 import Markup
from datetime import datetime, timedelta


class momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        return Markup(
            '<script>\ndocument.write(moment("%s").local().%s);\n</script>'
            % (self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), format)
        )

    def format(self, fmt):
        return self.render('format("%s")' % fmt)

    def calendar(self):
        return self.render("calendar()")

    def from_now(self):
        return self.render("fromNow()")

    def is_late(self, periodicity):
        currentTime = datetime.utcnow()
        lastExecTime = datetime.strptime(
            self.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
        )
        duration = (
            currentTime - lastExecTime
        ).total_seconds() / 3600.0  # result is in hour
        if (
            (periodicity.lower() == "hourly" and duration >= 1)
            or (periodicity.lower() == "daily" and duration >= 24)
            or (periodicity.lower() == "weekly" and duration >= 168)
            or (periodicity.lower() == "monthly" and duration >= 730)
        ):
            return True
        return False

    def is_soon(self, periodicity):
        current_time = datetime.utcnow()
        next_exec_time = self.next_time(periodicity)
        duration = (
            next_exec_time - current_time
        ).total_seconds() / 60.0  # result is in minutes
        if duration <= 0:
            return False

        if (
            (periodicity.lower() == "hourly" and duration <= 10)
            or (periodicity.lower() == "daily" and duration <= 60)
            or (periodicity.lower() == "weekly" and duration <= 1080) # 18hrs
            or (periodicity.lower() == "monthly" and duration <= 1080) # 18hrs
        ):
            return True
        return False

    def next_time(self, periodicity):
        last_exec_time = datetime.strptime(
            self.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
        )
        if periodicity.lower() == "hourly":
            return last_exec_time+timedelta(hours=1)
        if periodicity.lower() == "daily":
            return last_exec_time+timedelta(days=1)
        if periodicity.lower() == "weekly":
            return last_exec_time+timedelta(days=7)
        if periodicity.lower() == "monthly":
            return last_exec_time+timedelta(weeks=1)
