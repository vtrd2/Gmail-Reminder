import json, os
class Database():
    '''cuida do banco de dados'''
    def __init__(self):
        self.file = 'json_calendary.json'
        self.dict_calendary, self.dict_calendary_one_day_before = self.download()
    
    def download(self):
        '''Faz o download dos dados'''
        with open(self.file, 'r') as file_obj:
            dict_calendary, dict_calendary_one_day_before = json.load(file_obj)
            return dict_calendary, dict_calendary_one_day_before
    
    def save(self):
        with open(self.file, 'w') as file_obj:
            json.dump([self.dict_calendary, self.dict_calendary_one_day_before], file_obj)
    
    @staticmethod
    def cria_json(file):
        '''Cria o arquivo .json se não existir'''
        if not os.path.exists(file):
            file_obj = open(file, 'w')
            json.dump([{}, {}], file_obj)
            file_obj.close()