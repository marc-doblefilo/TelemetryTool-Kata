import pytest

from models.track import Track

def test_track_init():
    imola = Track('Emilia-Romagna GP', 72.452, 88.665)

    assert imola.name == 'Emilia-Romagna GP'
    assert imola.minimumTime == 72.452
    assert imola.maximumTime == 88.665
