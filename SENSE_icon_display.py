#!/usr/bin/env python3

from sense_hat import SenseHat
import time
import glob
# import random

sense = SenseHat()

sense.set_rotation(180)

for filename in glob.glob("*.jpg"):
    sense.clear()
    sense.load_image(filename)
    time.sleep(10)

sense.clear()
