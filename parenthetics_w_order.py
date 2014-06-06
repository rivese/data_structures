#!/usr/bin/python

def paranth_n (str_) :
    if not len(str_) :
        return
    hasparant = False
    size = 0

    for i in range(len(str_)):
        if str_[i] == '(':
            hasparant = True
            size += 1
        elif str_[i] == ')':
            hasparant = True
            if size == 0 :
                return -1
            size -= 1
    if size == 0 :
        if hasparant == False :
            print u"There is no paranthesis in the given string"
            return
        return 0
    if size > 0 :
        return 1
    return -1




def paranth_logn (str_):
    if not len(str_):
        print u"String is empty"
        return
    # Checking if there is any parantesis
    if not str_.count('(') and not str_.count(')') :
        print u"There is no paranthesis in the given string"
        return
    # Checking if there is only one kind paranthesis or the count difference is not 0
    if (not str_.count('(') or not str_.count(')')) or abs(str_.count('(')-str_.count(')')) :
        if str_.count('(') > str_.count(')') :
            return 1
        else :
            return -1

    l = len(str_)
    print l
    size = 0

    # in this for loop order of if 's are important
    for i in range(l//2) :
        if str_[i] == ')' :
            if not size :
                return -1
            size -=1
        if str_[i] == '(' :
            size += 1
        if str_[l-i-1] == '(' :
            if not size:
                return 1
            size += 1
        if str_[l-i-1] == ')' :
            size -= 1

    if l%2 :
        if str_[l//2]== ('(') :
            size += 1
        elif str_[l//2]== (')') :
            size -=1
    if size == 0 :
        return 0
    if size > 0 :
        return 1
    return -1


def paranth_eff (str_):
    if not len(str_) :
        print u"String is empty"
        return
    # Checking if there is any parantesis
    if not str_.count('(') and not str_.count(')') :
        print u"There is no paranthesis in the given string"
        return
    # Checking if there is only one kind paranthesis or the count difference is not 0
    if (not str_.count('(') or not str_.count(')')) or abs(str_.count('(')-str_.count(')')) :
        if str_.count('(') > str_.count(')') :
            return 1
        else :
            return -1

    end = len(str_)
    start_open = 0
    start_close = 0
    size = 0
    while True :
        try :
            start_open = str_.index('(',start_open, end)
            size += 1
        except ValueError :
            break
        try :
            start_close = str_.index(')', start_close, end)
            size -= 1
        except ValueError:
            break
        if start_open > start_close :
            return -1
        start_open += 1
        start_close += 1

    if size == 0 :
        return 0
    if size > 0:
        return 1
    return -1




if __name__ == '__main__' :
    s1 = ""
    s2 = "this is a some stupid string without paranthetics"
    s3 = "thi((s i(s) (a s))ome() st(upid st)ri(n)g with)out paranthetics"
    s4 = "thi((s i(s (a s))ome() st(upid st)ri(n)g with)out paranthetics"
    s5 = "thi((s i(s) (a s))ome() stupid st)ri(n)g with)out paranthetics"
    s6 = ")("
    s7 = "((()"
    s8 = "(())()"

    #print paranth_n(s6)
    print paranth_logn(s6)
    #print paranth_eff(s5)









