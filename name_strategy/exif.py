#!./env/bin/python
import datetime
import piexif

MODULE_NAME = "EXIF"

def _date_from_image(image):
    exif_dict = piexif.load(image)
    date = exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal]
    return datetime.datetime.strptime(str(date), "b'%Y:%m:%d %H:%M:%S'")

def kwargs_from_image(image):
    date = _date_from_image(image)
    return {'year': date.year, 'month': str(date.month).rjust(2, '0'), 'day': str(date.day).rjust(2, '0'), 'hour': str(date.hour).rjust(2, '0'), 'minute': str(date.minute).rjust(2, '0'), 'second': str(date.second).rjust(2, '0')}
