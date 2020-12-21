def last_ind(lst):
    if len(lst) == 0:
        return 'hola'
    return lst[-1]

def assert_equals(a, b):
    assert a == b

def test_last_ind():
    assert_equals(last_ind([0, 4, 19, 34, 50, -9, 2]), 2)
    assert_equals(last_ind(["Hello", "There", "Python", "User"]), "User")
    assert_equals(last_ind([]), None)
    assert_equals(last_ind([True, False, False, True]), True)
    assert_equals(last_ind([(5, 0), (0, 5, 6, 7), (3, 5, 67, 7), (0, -9, 3, 45, 5)]), (0, -9, 3, 45, 5))
    assert_equals(last_ind("Python is a great programming langauge."), ".")
    assert_equals(last_ind(["H", "E", "L", "L", "O"]), "O")
    assert_equals(last_ind("The quick brown fox jumped over the lazy dog"), "g")
    assert_equals(last_ind([{"name": "batman"}, {"kids": "none"}, {"parents": "also none"}]), {"parents": "also none"})
    assert_equals(last_ind(""), None)
