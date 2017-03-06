"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head is None:
            return None
        elif self.head.next:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            return tmp
        else:
            tmp = self.head
            self.head = None
            return tmp

    def get_head(self):
        return self.head

class Stack(object):
    count = 0

    def __init__(self, top=None):
        if top is not None:
            self.count += 1
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.count += 1
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        self.count -= 1
        return self.ll.delete_first()

    def size(self):
        return self.count

    def get_head(self):
        return self.ll.get_head()

if __name__ == "__main__":
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)