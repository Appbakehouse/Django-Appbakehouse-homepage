from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image, ImageOps
import os

def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)

class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)
    
    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        image = Image.open(self.path)

        size = (128, 128)
        image.thumbnail(size, Image.ANTIALIAS)

        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background
            
        image.save(self.thumb_path, 'JPEG') #, quality=95)

        #hint code 
        #fill_color = ''  # your background
        #image = Image.open(file_path)
        #if image.mode in ('RGBA', 'LA'):
        #    background = Image.new(image.mode[:-1], image.size, fill_color)
        #    background.paste(image, image.split()[-1])
        #    image = background
        #image.save(hidpi_path, file_type, quality=95)

        #before
        #background = Image.new('RGBA', size, (255, 255, 255, 0))
        #background.paste(img, ( int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2) ) )
        #background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)
