#!/usr/bin/python


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, value):
        self.head = Node(value)

    def print_allow(self):
        temp_node = self.head
        l = []
        while temp_node:
            l.append(temp_node.value)
            temp_node = temp_node.next
        print tuple(l) 

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        temp_node = self.head.next
        del self.head 
        self.head = temp_node 

    def size(self):
        count = 0
        temp_node = self.head
        while temp_node:
            count += 1
            temp_node = temp_node.next
        return count

    def search(self, value):
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return temp_node
            temp_node = temp_node.next
        return None

    def remove(self, node):
        if self.head == None:
            return 
        if self.head == node:
            self.pop()
        else:
            temp_node = self.head
            while temp_node.next:
                if temp_node.next == node:
                    temp_node.next.next = node.next
                    del node
                    break




if __name__ == '__main__':
    
    test = LinkedList(5)
    test.print_allow()
    test.insert(6)
    test.print_allow()
    test.size()
    new_node = test.search(6)
    test.remove(new_node)
    test.print_allow()
