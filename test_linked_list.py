#!/usr/bin/python


import linked_list as ll


def test_string():
    l = ll.LinkedList(7)

    assert str(l) == "(7)"


def test_insert():
    l = ll.LinkedList(7)
    l.insert(5)

    assert str(l) == "(5, 7)"
    print u'Passed insert test'


def test_pop():
    l = ll.LinkedList(7)
    l.insert(5)
   
    assert l.pop() == 5
    print u'Passed pop test'


def test_search():
    l = ll.LinkedList(7)
    l.insert(5)
    l.insert(8)
    l.insert('A')
    l.insert('B')
    l.insert('X')

    assert l.search(8).getdata() == 8
    assert l.search('A').getdata() == "A"
    
    print u'Passed search test'


def test_size():
    l = ll.LinkedList(7)
    l.insert(5)
    l.insert(8)

    assert l.size() == 3

    l.insert('A')
    l.insert('B')
    l.insert('X')

    assert l.size() == 6
    l.pop()
    assert l.size() == 5

    print u'Passed size test'


def test_remove():
    l = ll.LinkedList(7)
    l.insert(5)
    l.insert(8)
    l.insert(3)

    node = l.search(8)
    l.remove(node)

    assert str(l) == "(3, 5, 7)"

    print u'Passed remove test'



    


    