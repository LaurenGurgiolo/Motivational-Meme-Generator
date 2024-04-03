import os
from abc import ABC, abstractmethod

        
class IngestorInterface():
    '''Verifies the file type can be processed and does exist.'''
    
    def can_ingest(path, file_type):
        if file_type == 'json' or file_type == 'pdf':
            return True
        elif file_type == 'docx' or file_type == 'txt' or  file_type == 'csv':
            is_file = os.path.isfile(path)
            if is_file == True:
                return True 
            else:
                raise Exception('File does not exist')
       
    @abstractmethod
    def parse(path):
        file_type = path.split('.')[2]
        
        try:
            IngestorInterface.can_ingest(path, file_type)
        except Exception:
            print('Please try again wiith correct file type.')
        finally:
            return file_type
        
    
