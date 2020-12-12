import datetime

class Datetime():
    '''cuida do tempo'''
    def __init__(self):
        self.one_day = datetime.timedelta(days=1)
    
    def menos_um_dia(self, date):
        return date - self.one_day
    
    @staticmethod
    def strftime(date):
        date_str = date.strftime('%d/%m/%Y %H:%M')
        return date_str
    
    @staticmethod
    def strptime(date_str):
        date = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
        return date