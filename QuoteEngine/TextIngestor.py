from QuoteEngine.IngestorInterface import IngestorInterface

class TextIngestor(IngestorInterface):
    '''Takes a txt file and processes the contents into a list.'''
    def __init__(self, path):
        self.path = path
        
    def get_quotes(path, file_type):
        '''Returns a list with the quote str and author str.'''
        if IngestorInterface.parse(path):
            text_list = []
            file = open(path, "r")
            content = file.read()
            content = content.split('\n')
            for item in content:
                item = item.split(',')
                for x in item:
                    x = x.strip('\ufeff')
                    text_list.append(x)
            return text_list

