"""
Start Project Cars, run python speed.py and drive around in the game .. You should see values changing in your
console that indicate the speed for the car.
"""

import pypcars2api
import time

game = pypcars2api.live()

while True:
    print("Speed: " + str(round(game.mSpeed, 1)) + " m/s")
    time.sleep(0.5)
