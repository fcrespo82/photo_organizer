#!./env/bin/python
import re

MODULE_NAME = "FILENAME"

DATES_FORMAT = [r".*(?P<day>\d{2}).(?P<month>\d{2}).(?P<year>\d{4}).(?P<hour>\d{2}).(?P<minute>\d{2}).(?P<second>\d{2}).*"]

class Dynamic:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

def _date_from_filename(image):
    for date_format in DATES_FORMAT:
        match = re.match(date_format, image)
        if match:
            date = Dynamic(**match.groupdict())
    return date

def kwargs_from_image(image):
    #pylint: disable=I0011,E1101
    date = _date_from_filename(image)
    return {'year': date.year, 'month': str(date.month).rjust(2, '0'), 'day': str(date.day).rjust(2, '0'), 'hour': str(date.hour).rjust(2, '0'), 'minute': str(date.minute).rjust(2, '0'), 'second': str(date.second).rjust(2, '0')}
