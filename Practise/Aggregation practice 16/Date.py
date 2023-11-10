import datetime
class Date:
    def __init__(self):
        date = datetime.datetime.now()
        self.day = date.day
        self.month= date.month
        self.year= date.year

    def __str__(self):
        return f'Date:- day:{self.day} Month: {self.month} Year: {self.year}'

    def set_day(self, day):
        self.day = day

    def set_month(self,month):
        self.month=month

    def set_year(self,year):
        self.year=year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year


