#!/usr/bin/python


import stack


def test_string():
    s = stack.Stack (7)
    assert str(s) == "(7)"

def test_insert():
    s = stack.Stack (7)
    s.insert(5)
    assert str(s) == "(5, 7)"

    s.pop()
    s.pop()
    s.insert(4)
    assert str(s) == "(4)"
    print u'Passed insert test'


def test_pop():
    s = stack.Stack(5)
    assert s.pop() == 5
    assert s.pop() == None
    print u'Passed pop test'

