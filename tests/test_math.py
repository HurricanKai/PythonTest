from testpkg.math import inc, add


def test_answer():
    assert inc(3) == 4


def test_add_simple():
    assert add(1, 2) == 3


def test_add_large():
    assert add(1000000000000000, 2) == 1000000000000002


def test_add_negative():
    assert add(-10000, 2) == -9998
