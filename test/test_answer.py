def inc(x):
    return x + 1

def sub(x):
    return x - 1

def test_answer():
    assert inc(3) == 5

def test_inc():
    assert inc(3) == 4

def test_toto():
    assert inc(4) == 5

def test_tata():
    assert inc(6) == 8

def test_titi():
    assert inc(8) == 8

def test_sub():
    assert sub(4) == 3

def test_sub_1():
    assert sub(8) == 3


def test_clem():
    assert sub(5) == 4