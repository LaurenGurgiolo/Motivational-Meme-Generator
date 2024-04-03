from PIL import Image, ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
import random


class TextOn():
    '''Prints text on the image.'''
    def text_on_img(tmp_path, text, author):
        with Image.open(tmp_path) as quote_img:
            quote_img.load()
            quote_img.show()
            w, h = quote_img.size
            quote_text = ImageDraw.Draw(quote_img)
            myFont = ImageFont.truetype('FreeMonoBold.ttf', 20)
            x = random.randint(0, int(w-350))
            y = random.randint(0, int(h/5))
            text = text + '\n' + author
            quote_text.text((x, y), text, font=myFont, fill =(244, 172, 179), stroke_width=2, stroke_fill=(113, 12, 22))
            quote_img.save(tmp_path, 'JPEG')
            
            
            
