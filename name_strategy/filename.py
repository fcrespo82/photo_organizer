#!./env/bin/python
import datetime
import re

MODULE_NAME = "FILENAME"

DATES_FORMAT = [r".*(?P<day>\d{2}).(?P<month>\d{2}).(?P<year>\d{4}).(?P<hour>\d{2}).(?P<minute>\d{2}).(?P<second>\d{2}).*"]

def _date_from_filename(image):
    for date_format in DATES_FORMAT:
        try:
            match = re.match(date_format, image)
            if match:
                date = match.groupdict()
        except:
            pass
    return date

def kwargs_from_image(image):
    date = _date_from_filename(image)
    return {'year': date.year, 'month': str(date.month).rjust(2, '0'), 'day': str(date.day).rjust(2, '0'), 'hour': str(date.hour).rjust(2, '0'), 'minute': str(date.minute).rjust(2, '0'), 'second': str(date.second).rjust(2, '0')}
