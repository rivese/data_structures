#!/usr/bin/python


import stack

def test_init():
    try :
        x = stack.Stack()
    except TypeError :
        print u"Passed init test"
    s = stack.Stack(3)
    assert str(s.head.data) == "3"

    s.push(5)
    assert str(s.head.next.data) == '3'
    assert str(s.head.data) == '5'

def test_push():
    s = stack.Stack (7)
    s.push(5)
    assert str(s.head.data) == '5'
    assert str(s.head.next.data) == '7'

    s.pop()
    s.pop()
    s.push(4)
    assert str(s.head.data) == '4'
    print u'Passed insert test'


def test_pop():
    s = stack.Stack(5)
    assert s.pop() == 5
    assert s.pop() == None
    print u'Passed pop test'

