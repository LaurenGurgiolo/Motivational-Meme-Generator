class QuoteModel():
    '''Create a class object from the inputs:
    body = string 
    author = string'''
    def __init__(self, body, author):
        self.body = body
        self.author = author
        
    def __str__(self):
        return f'\nQuote of the day!\n{self.body}\n{self.author}'
        
        
    def __repr__(self):
        return f'QuoteModel(quote={self.body}, author={self.author})\n'
        
        
