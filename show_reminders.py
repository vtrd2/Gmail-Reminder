from database_py import *

class Show_Reminders():
    def __init__(self):
        self.database = Database()
    
    def show(self):
        print()
        dict_calendary = self.database.dict_calendary
        if len(dict_calendary) == 0:
            print("You don't have more active reminders")
        for date, description in dict_calendary.items():
            print(f'{date} - {description}')
        print()
        input('Press enter to continue:\n')