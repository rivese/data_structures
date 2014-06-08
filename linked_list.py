#!/usr/bin/python


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def getdata(self):
        return self.value

class LinkedList(object):
    def __init__(self, value):
        self.head = Node(value)
        self.size_ = 1

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.size_ += 1

    def pop(self):
        if not self.head :
            return
        elif not self.head.next :
            val = self.head.value
            self.head = None
            self.size_ = 0
            return val
        else :
            val, self.head = self.head.value, self.head.next
            self.size_ -= 1
        return val

    def size(self):
        return self.size_

    def search(self, value):
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return temp_node
            temp_node = temp_node.next
        else :
            return None

    def remove(self, node):
        if not self.head :
            return u"Link List is empty!"
        if self.head == node:
            return self.pop()
        temp_node = self.head
        while temp_node.next:
            if temp_node.next == node:
                temp_node.next = node.next
                break
        else :
            return u"Node is not in the Link List"

    def __str__(self):
        tmp_node = self.head
        str_ = "("
        while tmp_node :
            str_ += str(tmp_node.value) + ", "
            tmp_node = tmp_node.next
        return str_[:-2]+")" if len(str_)>1 else str_+")"


if __name__ == '__main__':
    test = LinkedList(5)
    test.insert(6)
    print test.search('X')
    print test
    test.size()
    new_node = test.search(6)
    test.remove(new_node)
    print test
    print test.pop()
    print test.pop()
    print test
