#!/usr/bin/python

from parenthetics_w_order import paranth_n
from parenthetics_w_order import paranth_logn
from parenthetics_w_order import paranth_eff


def test_parenthetics ():
    s1 = ""
    s2 = "this is a some stupid string without paranthetics"
    s3 = "thi((s i(s) (a s))ome() st(upid st)ri(n)g with)out paranthetics"
    s4 = "thi((s i(s (a s))ome() st(upid st)ri(n)g with)out paranthetics"
    s5 = "thi((s i(s) (a s))ome() stupid st)ri(n)g with)out paranthetics"
    s6 = ")("
    s7 = "((()"
    s8 = "(())()"

    slist = [(s1,None), (s2,None), (s3,0), (s4,1), (s5,-1), (s6,-1), (s7,1), (s8,0)]

    for i in slist:
        assert paranth_n(i[0]) == i[1]
        assert paranth_logn(i[0]) == i[1]
        assert paranth_eff(i[0]) == i[1]

    print u'All Tests passed'

