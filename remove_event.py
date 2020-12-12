from datetime_py import *
from database_py import *

class Rm_Date():
    '''Responsavel por remover datas'''
    def __init__(self):
        self.database = Database()
        self.datetime = Datetime()
    
    def print_reminders(self):
        list_of_dictionary = self.database.dict_calendary.items()
        if len(list_of_dictionary) >= 1:
            value = 1
            print()
            for date, text in self.database.dict_calendary.items():
                print(f'[{value}] - {date}, {text}')
                value += 1
            print()
        else:
            print("\nYou have no reminders to delete.\n")

    def recive_data(self):
        while True:
            self.print_reminders()
            index = input('Enter the reminder number to delete, press enter to cancel: ')
            if not index.split():
                return None
            try:
                index = int(index) - 1
            except Exception:
                print('\nYou entered something wrong')
                continue   
            if 0 <= index < len(self.database.dict_calendary):
                return index
            else:
                print('\nYou enter something wrong\n')
    
    def delete_reminder(self):
        index = self.recive_data()
        if index != None:
            data_str = list(self.database.dict_calendary.keys())[index]

            date_obj = self.datetime.strptime(data_str)
            date_obj_one_day_before = self.datetime.menos_um_dia(date_obj)
            one_day_before = self.datetime.strftime(date_obj_one_day_before)

            del self.database.dict_calendary[data_str]
            if one_day_before in self.database.dict_calendary_one_day_before.keys():
                del self.database.dict_calendary_one_day_before[one_day_before]

            self.database.save()

if __name__ == "__main__":
    remove_date = Rm_Date()
    remove_date.delete_reminder()