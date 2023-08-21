import datetime 
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse


class DateLocate(object):

    @staticmethod
    def parse(date_string):
        d0 = DateLocate()
        d0.date = parse(date_string)
        return d0

    def __init__(self):
        self.date = datetime.datetime.now()

    def format(self, expression):
        return self.date.strftime(expression)
    
    def year(self, year):
        self.date = self.date.replace(year=year)
        return self
    
    def month(self, month):
        self.date = self.date.replace(month=month)
        return self
    
    def day(self, day):
        self.date = self.date.replace(day=day)
        return self
    
    def hour(self, hour):
        self.date = self.date.replace(hour=hour)
        return self
    
    def minute(self, minute):
        self.date = self.date.replace(minute=minute)
        return self
    
    def second(self, second):
        self.date = self.date.replace(second=second)
        return self
    
    def week(self, week):
        # week 星期，从1到7，分别表示周一至周日 
        return self.add(days=week - self.date.weekday() - 1)
    
    def lastDay(self):
        self.add(months=1).day(1).add(days=-1)
        return self

    def add(self, seconds: int=0, minutes: int=0, hours: int=0, days: int=0, weeks: int=0, months: int=0, years: int=0):
        if seconds != 0:
            self.date = self.date + datetime.timedelta(seconds=seconds)

        if minutes != 0:
            self.date = self.date + datetime.timedelta(minutes=minutes)

        if hours != 0:
            self.date = self.date + datetime.timedelta(hours=hours)

        if days != 0:
            self.date = self.date + datetime.timedelta(days=days)
        
        if weeks != 0:
            self.date = self.date + datetime.timedelta(days=weeks*7)

        if months != 0:
            self.date = self.date + relativedelta(months=months)

        if years != 0:
            self.date = self.date + relativedelta(years=years)

        return self
