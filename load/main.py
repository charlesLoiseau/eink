import sys
import os

from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw


epd = epd7in5_V2.EPD()
epd.init()

Himage = Image.new('1', (epd.width, epd.height), 255)
bmp = Image.open('/home/pi/screen/eink.png')

bmp.show()
Himage.paste(bmp, (0,0))
epd.display(epd.getbuffer(Himage))
