from testpkg.math import inc, sub


def test_answer():
    assert inc(3) == 4


def test_subtraction_simple():
    assert sub(2, 1) == 1


def test_subtraction_large():
    assert sub(100000000000, 1) == 99999999999


def test_subtraction_negative():
    assert sub(-5, -3) == -2
