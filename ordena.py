import datetime

class Ordena():
    @staticmethod
    def ordena_dicts(dictionary):
        new_dict = {}

        date_list = Ordena.list_to_date_list(list(dictionary.keys()))
        text_list = Ordena.date_list_to_list(date_list)
        for date in text_list:
            dicionario = dictionary[date]
            new_dict[date] = dicionario

        return new_dict
    
    @staticmethod
    def list_to_date_list(lista):
        new_list = []
        for key in lista:
            key = datetime.datetime.strptime(key, '%d/%m/%Y %H:%M')
            new_list.append(key)
        return sorted(new_list)
    
    @staticmethod
    def date_list_to_list(lista):
        new_list = []
        for date in lista:
            key = date.strftime('%d/%m/%Y %H:%M')
            new_list.append(key)
        return new_list