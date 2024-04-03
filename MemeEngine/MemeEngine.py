from MemeEngine.Resize import Resize
from MemeEngine.TextOn import TextOn
import random


class MemeEngine():
    '''Resizes the image and puts text on the image.'''
    def __init__(self, tmp_path = './static/static'):
        self.tmp_path = tmp_path +  f'{random.randint(0, 100000)}.jpeg'
        
    def make_meme(self, img_path, text, author, width=500):
        tmp_path = self.tmp_path
        Resize.resize_img(img_path, tmp_path, width=500)
        TextOn.text_on_img(tmp_path, text, author)
        return self.tmp_path
        
      
        
    