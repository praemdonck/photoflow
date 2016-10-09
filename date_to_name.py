#! /usr/bin/env python2

import glob
import datetime
from gi.repository import GExiv2
import os

#image_list = glob.glob("IMG_9*")
image_list = glob.glob("*.JPG")

for i in image_list:
  try:
    p = GExiv2.Metadata(i)
    date_time = p.get_date_time()
    name_string = date_time.strftime("%Y%m%d_%H%M%S")
    b, e = os.path.splitext(i)
    e = ".JPG"
    name_string += e
    print name_string + " " + i
    if not os.path.isfile(name_string):
      os.rename(i, name_string)
    else:
      print "File %s already exists" % name_string
  except:
    pass

