import pytest
from Core.landmark import Landmark

def test_init():
    lm = Landmark()
    assert not lm._position
