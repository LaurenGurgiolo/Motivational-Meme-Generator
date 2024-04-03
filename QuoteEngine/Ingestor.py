from QuoteEngine.JsonIngestor import JsonIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.MakeQuote import MakeQuote

        
class Ingestor():
    '''Uses the file type of the path to call the appropriate module to process the contents of the file.'''
    def parse(path):
        '''Gets the file type from the path.'''
        file_type = path.split('.')[2]
        return Ingestor.quotes_from_filetype(path, file_type)
        
      
    def quotes_from_filetype(path, file_type):
        '''Calls the appropriate module for the file type.'''
        quote_list = []
        if file_type  == 'json': text = JsonIngestor.get_quotes(path, file_type)
        if file_type  == 'csv' or file_type  == 'csv1': text = CSVIngestor.get_quotes(path, file_type)
        if file_type  == 'pdf': text = PDFIngestor.get_quotes(path, file_type)
        if file_type  == 'docx': text = DocxIngestor.get_quotes(path, file_type)
        if file_type  == 'txt': text = TextIngestor.get_quotes(path, file_type)
                
        quote_list  = MakeQuote.edit_body(text)
       
        return quote_list
    