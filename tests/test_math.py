from testpkg.math import inc, add, sub


def test_answer():
    assert inc(3) == 4


def test_add_simple():
    assert add(1, 2) == 3


def test_add_large():
    assert add(1000000000000000, 2) == 1000000000000002


def test_add_negative():
    assert add(-10000, 2) == -9998


def test_subtraction_simple():
    assert sub(2, 1) == 1


def test_subtraction_large():
    assert sub(100000000000, 1) == 99999999999


def test_subtraction_negative():
    assert sub(-5, -3) == -2
