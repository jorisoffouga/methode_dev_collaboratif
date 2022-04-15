def inc(x):
    return x + 1

def sub(x):
    return x - 1


def test_answer():
    assert inc(3) == 5

def test_inc():
    assert inc(3) == 4

def test_sub():
    assert sub(2) == 1

def test_sub_pt():
    assert sub(3) == 1