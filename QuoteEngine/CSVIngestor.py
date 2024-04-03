import pandas
import datasets
from datasets import load_dataset
from QuoteEngine.IngestorInterface import IngestorInterface
    

class CSVIngestor(IngestorInterface):
    '''Takes a CVS file and processes the contents into a dictionary.'''
    def __init__(self, path):
        self.path = path
        '''dataset = load_dataset("datastax/philosopher-quotes")'''
        
   
    def get_quotes(path, file_type):
        '''Returns a dictionary with the quote str as the key and author str as the value.'''
        if IngestorInterface.parse(path):
            quote_dict = {}
            if '1' in file_type:
                path = "datastax/philosopher-quotes"
                dataset = load_dataset(path)
                dataset = dataset.remove_columns("tags")
                flat_dataset = dataset.flatten()
                pd = datasets.Dataset.to_pandas(dataset['train'])
                for index, row in pd.iterrows():
                    quote_dict[row['quote']]  = row['author']
                return quote_dict
        
