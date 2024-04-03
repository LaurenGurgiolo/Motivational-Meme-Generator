from QuoteEngine.quotes import QuoteModel

class MakeQuote():
    '''Edits the body text dependent on collection type and formats the content to create a QuoteModel class object.'''    
    def edit_body(text):  
        quote_list = []
        if type(text) is list:
            for item in text:
                if item != '':
                    body,author = item.split('-')
                    body = body.split(" ")
                    return_str = '\n'
                    x = 0
                    for index, word in enumerate(body):
                        if index%5 == 0:
                            x+=1
                            if x >= 10:
                                break
                            else:
                                body.insert(index, return_str )
                    body = (" ").join(body)
                    quote = QuoteModel(body, author)
                    quote_list.append(quote)
                
        else:  
            for body, author in text.items():
                body = body.split(" ")
                return_str = '\n'
                x= 0
                for index, word in enumerate(body):
                    if index%5 == 0:
                        x+=1
                        if x >= 12:
                            break
                        else:
                            body.insert(index, return_str )
                body = (" ").join(body)
                quote = QuoteModel(body, author)
                quote_list.append(quote)
        return quote_list

