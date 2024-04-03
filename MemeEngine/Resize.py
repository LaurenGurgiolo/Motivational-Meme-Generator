from PIL import Image, ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
import os




class Resize():
    '''Resize image.'''
    def resize_img(img_path, tmp_path, width=500):
        with Image.open(img_path) as img:
            img.load()
            img.show()
            basewidth = width
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize))
            img = img.filter(ImageFilter.BLUR)
            img.save(tmp_path, 'JPEG')
            
        
    
    