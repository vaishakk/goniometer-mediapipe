from Core.utils import dotproduct, abs
import pytest

def test_dotproduct():
    assert dotproduct((1,2), (3,2)) == 7

def test_abs():
    assert abs((3,4)) == 5