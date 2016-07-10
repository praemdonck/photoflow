#! /usr/bin/env python2

import glob
import datetime
from gi.repository import GExiv2

image_list = glob.glob("IMG_3*.*")
#time_offset = datetime.timedelta(-1, 59274)
time_offset = datetime.timedelta(-89, 12504)

for i in image_list:
  p = GExiv2.Metadata(i)
  date_time = p.get_date_time()
  corrected_time = date_time + time_offset
  print i + " " + str(date_time) + " " + str(corrected_time)
  p.set_date_time(corrected_time)
  p.save_file(i)
  
