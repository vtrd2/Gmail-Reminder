import re
from database_py import *
from datetime_py import *
from ordena import Ordena
from remove_special_characters import TextUtil

pattern = re.compile(r'\d\d/\d\d/\d\d\d\d\s\d\d:\d\d')

class Add_Reminder():
    '''Classe responsavel pelo recebimento de dados'''
    def __init__(self):
        self.database = Database()
        self.datetime = Datetime()

    @staticmethod    
    def questions():
        '''Faz as perguntas da data'''
        date = input('\nEnter the date in dd/mm/yyyy format, press just enter to cancel:\n').replace('-', '/')
        hour = input('\nEnter the time in 24-hour format and in hh:mm, press just enter to cancel:\n')
        return date, hour
    
    @staticmethod
    def question_description():
        description = input('\nEnter the description of event:\n')
        description = TextUtil.remove_special_characters(description)
        return description

    def recive_data(self):
        '''Verifica se as respostas estão padronizadas, e as formata'''
        while True:
            date, hour = self.questions()
            if date.strip() == '' or hour.strip() == '':
                return None

            date_hour = f'{date} {hour}'
            try:
                datetime_obj = self.datetime.strptime(date_hour)
                if datetime_obj < datetime.datetime.now():
                    raise('Data passada')
                if not pattern.search(date_hour):
                    raise('Não segue o padrão')
            except Exception:
                print('''\nYou entered something wrong in the date or in the hour, make sure you haven't entered a past date, please try more once.''')
            else:
                break
        
        one_day_before = self.datetime.menos_um_dia(datetime_obj)

        if one_day_before <= datetime.datetime.now():
            one_day_before = None
        else:
            one_day_before = self.datetime.strftime(one_day_before)
        description = self.question_description()
        return date_hour, one_day_before, description
    
    def add_date_database(self, date_hour, one_day_before, description):
        self.database.dict_calendary[date_hour] = description
        if one_day_before != None:
            self.database.dict_calendary_one_day_before[one_day_before] = description
    
    def add_reminder_execute(self):
        recived_data = self.recive_data()
        if recived_data == None:
            return 
        date_hour, one_day_before, description = recived_data
        self.add_date_database(date_hour, one_day_before, description)
        self.database.save()



if __name__ == "__main__":
    add_reminder = Add_Reminder()
    add_reminder.add_reminder_execute()
