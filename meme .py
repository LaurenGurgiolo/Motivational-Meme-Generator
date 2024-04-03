import os
import random
import argparse
from urllib.error import *
import requests
from QuoteEngine.Ingestor import Ingestor
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.quotes import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   '.https://philosophyapipythonanywherecom/api/philosophers/1/.json',
                   '.datastax/philosopher-quotes.csv1',
                   './_data/PhilosophyQuotes/seneca.pdf']
    quotes = []
    if body is None or body == 'none':
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))
            quote = random.choice(quotes)
    if body:
        if author is None or author == '':
            raise Exception('Author Required if Body is Used')
        else:
            quote = QuoteModel(body, author)
    print(quote)
    if path is None or path == 'None,':
        path = './static/static'
        images = "./_data/photos/graves/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    elif path:
        img = path
        path = './static/static'

    meme = MemeEngine(path)
    path = meme.make_meme(img, quote.body, quote.author)
    return path



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", default= None, help='Image URL address for image of meme, random if not specified.') 
    parser.add_argument("-body",default= None, help='A quote to print on image, random if not specified.')
    parser.add_argument("-author", default= None, help='The author of the quote- required if -body added.')
    args = parser.parse_args()
   
    
    try:
        res = requests.get(args.path, stream = True)
    except HTTPError as e:
        path = None
        print(e, 'Random image will be used.')
    except URLError as e:
        path = None
        print(e, 'Random image will be used.')
    except ValueError as e:
        path = None
        print(e, 'Random image will be used.')
    except requests.exceptions.ConnectionError as e:
        path = None
        print(e, 'Random image will be used.')
    except requests.exceptions.InvalidURL as e:
        path = None
        print(e, 'Random image will be used.')
    else:
        data = requests.get(args.path).content
        f = open('static/tmp.jpeg','wb')
        f.write(data) 
        f.close()
        path = 'static/tmp.jpeg'
    

    body = None
    author = None
    if args.body is not None and args.body != 'none': body = args.body
    if args.author is not None and args.author != 'none':  author = args.author
    img = generate_meme(path=path, body=body, author=author)
    print(img)