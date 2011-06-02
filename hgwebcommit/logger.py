# coding: utf-8
import time
from datetime import datetime

from logging.handlers import TimedRotatingFileHandler

def get_next_month_first_day(now=None):
    if not now:
        now = datetime.now()
    year = now.year
    month = now.month
    month += 1
    # next year
    if month > 12:
        year += 1
        month = 1
    return datetime(year, month, 1, 0, 0, 0, 0)

def datetime_to_time(d):
    return time.mktime(d.timetuple())

class MonthlyRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, *args, **kwargs):
        TimedRotatingFileHandler.__init__(self, *args, **kwargs)
        self.rolloverAt = self.get_next_rollover_at()

    def doRollover(self):
        TimedRotatingFileHandler.doRollover(self)
        self.rolloverAt = self.get_next_rollover_at()

    def get_next_rollover_at(self):
        return datetime_to_time(get_next_month_first_day())

