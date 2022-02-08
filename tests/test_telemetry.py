from models.telemetry import Telemetry
import pytest

from models.driver import Driver
from models.track import Track

def test_telemetry_init():
    max = Driver('Max Verstappen', 1)
    imola = Track('Imola GP', 67.345, 77.234)
    telemetry = Telemetry(max, imola)

    assert telemetry.driver.name == max.name
    assert telemetry.track.name == imola.name

def test_telemetry_setQualiTime():
    max = Driver('Max Verstappen', 1)
    imola = Track('Imola GP', 67.345, 77.234)
    telemetry = Telemetry(max, imola)

    telemetry.setQualiTime()

    assert telemetry.qualiTime > imola.minimumTime
    assert telemetry.qualiTime < imola.maximumTime
