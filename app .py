import random
import os
from urllib.error import *
import requests
from flask import Flask, render_template, abort, request
from meme import generate_meme
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor



app = Flask(__name__)

meme = MemeEngine('./static/static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
'.https://philosophyapipythonanywherecom/api/philosophers/1/.json',
                      '.datastax/philosopher-quotes.csv1',
                      './_data/PhilosophyQuotes/seneca.pdf']
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))
    images = "./_data/photos/graves/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    quote = random.choice(quotes)
    img = random.choice(imgs)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    try:
        responce = request.form.get("image_url")
        res = requests.get(responce, stream = True)
    except HTTPError:
        path = None
    except URLError:
        path = None
    except ValueError:
        path = None
    else:
        data = requests.get(responce).content
        file = open('./tmp.jpeg','wb')
        file.write(data)
        file.close()
        path = './tmp.jpeg'
    body = request.form.get('body')
    if not body: body = None
    author = request.form.get('author')
    if not author: body = None
    path_final = generate_meme(path, body, author)
    return render_template('meme.html', path=path_final)

if __name__ == "__main__":
    app.run()
    