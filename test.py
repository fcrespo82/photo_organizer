#!./env/bin/python

import name_strategy.exif
import name_strategy.filename

print(name_strategy.exif.kwargs_from_image('./teste/IMG_0357.JPG'))

print(name_strategy.filename.kwargs_from_image('./teste/IMG_22.10.2016.10.10.10.JPG'))
