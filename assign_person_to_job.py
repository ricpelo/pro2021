def assign_person_to_job(names, jobs):
    return dict(zip(names, jobs))

def assert_equals(a, b):
    assert a == b

def test_xxx():
    pl = ["Annie", "Steven", "Lisa", "Osman"]
    jl = ["Teacher", "Engineer", "Doctor", "Cashier"]
    assert_equals(assign_person_to_job(pl, jl), {'Annie': 'Teacher', 'Steven': 'Engineer', 'Lisa': 'Doctor', 'Osman': 'Cashier'})
