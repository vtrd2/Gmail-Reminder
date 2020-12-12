import json, datetime, threading, time
from send_email import Sending

class Data():
    '''Classe que cuida dos dados'''
    def __init__(self):
        self.data_file = 'json_calendary.json'
        self.dict_calendary = {}
        self.dict_calendary_one_day_before = {}
    
    def baixa_dados (self):
        '''baixa os dados do .json'''
        while True:
            with open(self.data_file, 'r') as file_obj:
                dict_calendary, dict_calendary_one_day_before = json.load(file_obj)
            self.dict_calendary = dict_calendary
            self.dict_calendary_one_day_before = dict_calendary_one_day_before
            time.sleep(1.5)
    
    def save_datas(self, dictionary1, dictionary2):
        with open(self.data_file, 'w') as file_obj:
            json.dump([dictionary1, dictionary2], file_obj)
    
    @staticmethod
    def dict_to_list_data(dictionary):
        new_list = []
        for date_str in dictionary.keys():
            date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
            new_list.append(date_obj)
        return new_list


class Remind():

    def __init__(self):
        self.data = Data()
        self.send = Sending()

    def remind_in_day(self):
        while True:
            dict_data_obj = Data.dict_to_list_data(self.data.dict_calendary)
            date_now = datetime.datetime.now()
            for date in dict_data_obj:
                if date <= date_now:
                    date_str = date.strftime('%d/%m/%Y %H:%M')
                    self.send.send_mail(f'Reminder: {date_str}', self.data.dict_calendary[date_str])
                    print('Sended email for today')
                    del self.data.dict_calendary[date_str]

                    self.save()
            time.sleep(2)

    def remind_one_day_before(self):
        while True:
            dict_data_obj = Data.dict_to_list_data(self.data.dict_calendary_one_day_before)
            date_now = datetime.datetime.now()
            for date in dict_data_obj:
                if date <= date_now:
                    date_str = date.strftime('%d/%m/%Y %H:%M')
                    message = f'Tomorrow, need to {self.data.dict_calendary_one_day_before[date_str]}'
                    self.send.send_mail(f'Reminder for tomorrow.', message)
                    print('Sended email for tomorrow')
                    del self.data.dict_calendary_one_day_before[date_str]

                    self.save()
            time.sleep(2)

    def execute(self):
        threading_download = threading.Thread(target=self.data.baixa_dados)
        threading_remind_in_day = threading.Thread(target=self.remind_in_day)
        threading_remind_one_day_before = threading.Thread(target=self.remind_one_day_before)

        threading_download.start()
        time.sleep(0.5)
        threading_remind_in_day.start()
        threading_remind_one_day_before.start()
    
    def save(self):
        self.data.save_datas(self.data.dict_calendary, self.data.dict_calendary_one_day_before)


if __name__ == "__main__":
    reminder = Remind()
    reminder.execute()