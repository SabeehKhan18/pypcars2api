"""
Start Project Cars 2, run python standing.py while doing a race.
"""

import pypcars2api
import time

game = pypcars2api.live()

while True:
    for player in game.standing():
        print(str(player['position']) + '. ' + player['name'] + ' (' + str(player['lap']) + "/" +
              str(game.mLapsInEvent) + ') (' + str(round(player['lap_distance'])) + ')')

    time.sleep(10)
    print("\n\n\n\n")
