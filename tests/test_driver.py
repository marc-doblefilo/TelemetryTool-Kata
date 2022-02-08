import pytest

from models.driver import Driver

def test_driver_init():
    alonso = Driver('Fernando Alonso', 14)

    assert alonso.name == 'Fernando Alonso'
    assert alonso.number == 14

def test_driver_change_number():
    alonso = Driver('Fernando Alonso', 14)

    assert alonso.number == 14

    alonso.changeNumber(1)

    assert alonso.number == 1
