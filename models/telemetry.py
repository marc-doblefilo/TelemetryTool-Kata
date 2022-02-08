from models.driver import Driver
from models.track import Track

from random import uniform

class Telemetry():

    def __init__(self, driver: Driver, track: Track):
        self.driver = driver
        self.track = track
        self.qualiTime = 0.0
        self.raceTime = 0.0

    def setQualiTime(self):
        time = uniform(self.track.minimumTime, self.track.maximumTime)

        formattedTime = "{:.3f}".format(time)
        self.qualiTime = float(formattedTime)
