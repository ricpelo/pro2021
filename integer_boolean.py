def integer_boolean(n):
    res = []
    for i in n:
        res.append(i == '1')
    return res

def integer_boolean_mejor(n):
    return [i == '1' for i in n]

def assert_equals(a, b):
    assert a == b

def test_xxx():
    assert_equals(integer_boolean("100101"), [True, False, False, True, False, True])
    assert_equals(integer_boolean("10"), [True, False])
    assert_equals(integer_boolean("001"), [False, False, True])
    assert_equals(integer_boolean(""), [])
    assert_equals(integer_boolean("111"), [True, True, True])
    assert_equals(integer_boolean("000"), [False, False, False])
    assert_equals(integer_boolean("10010110"), [True, False, False, True, False, True, True, False])
