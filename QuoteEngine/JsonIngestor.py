import requests
from pathlib import Path
from QuoteEngine.IngestorInterface import IngestorInterface
    
class JsonIngestor(IngestorInterface):
    '''Takes a Json file and processes the contents into a Dictionary.'''
    def __init__(self, path):
        self.path = path
         
            
    def get_quotes(path, file_type):
        '''Returns a dictionary with the quote str as the key and author str as the value.'''
        if IngestorInterface.parse(path):
            quote_dict = {}
            base = 'https://philosophyapi.pythonanywhere.com/api/philosophers'
            response = requests.get(base)
            response_dict = response.json()
            for entry in range(8):
                str_list = response_dict['results'][entry]['ideas']
                for quote in str_list:
                    quote_dict[quote] = response_dict['results'][entry]['name']
            return quote_dict

            
