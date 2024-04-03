import os
import subprocess
import random
from QuoteEngine.IngestorInterface import IngestorInterface
        
class PDFIngestor(IngestorInterface):
    '''Takes a docx file and processes the contents into a list.'''
    def __init__(self, path):
        self.path = path
        
    def get_quotes(path, file_type):
        '''Returns a list with the quote str and author str.'''
        if IngestorInterface.parse(path):
            text = []
            tmp = f'./{random.randint(0, 100000)}.txt'
            call = subprocess.call(['pdftotext', path, tmp])
            contents = open(tmp,'r')
            for line in contents.readlines():
                parse = line.strip('99 Quotes by\n')
                parse = line.strip("\n'")
                parse = line.strip('\x0cCONTENTS')
                parse = line.strip("'\n'")
                parse = line.strip('CONTENTS')
                parse = line.strip('99 Quotes by')
                parse = line.strip('99 Quotes by Seneca')
                parse = line.strip('1')
                parse = line.replace("\n", "")
                text.append(parse)
            author = text[10]
            os.remove(tmp)
            return PDFIngestor.make_dict(author, text)

        
    def make_dict(author, text):
        saved_entry = str()
        text_dict = {}
        for entry in text:
            entry = entry.strip('99 Quotes by')
            entry = entry.strip('1')
            if entry != '':
                if entry[0].isdigit():
                    entry = ''.join((x for x in entry if not x.isdigit()))        
                    entry = entry.strip('. ')
                    text_dict[entry] = author
                    saved_entry = entry  
                else:
                    if entry != '' and saved_entry != '':
                        if entry[0].isalpha():
                            del text_dict[saved_entry]
                            saved_entry = saved_entry + entry
                            text_dict[saved_entry] = author
                            
        return text_dict
    
