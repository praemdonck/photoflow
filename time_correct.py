#! /usr/bin/env python2

import glob
import datetime
from gi.repository import GExiv2


#class datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
picture_date = datetime.datetime(2017, 6, 27, 12)
actual_date = datetime.datetime(2017, 6, 27, 19)

print str(picture_date - actual_date)
time_offset = actual_date - picture_date




#image_list = glob.glob("IMG_3*.*")
image_list = glob.glob("*.JPG")
#timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
#time_offset = datetime.timedelta(-1, 59274)
#time_offset = datetime.timedelta(0, 10*3600)

for i in image_list:
  try:
    p = GExiv2.Metadata(i)
    date_time = p.get_date_time()
    corrected_time = date_time + time_offset
    print i + " " + str(date_time) + " " + str(corrected_time)
    p.set_date_time(corrected_time)
    p.save_file(i)
  except:
    pass
  
