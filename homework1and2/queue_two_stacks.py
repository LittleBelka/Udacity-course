from homework1and2.stack import Element, Stack

class Queue:

    def __init__(self, head=None):
        self.stack_1 = Stack(head)
        self.stack_2 = None

    def enqueue(self, new_element):
        self.stack_1.push(new_element)

    def dequeue(self):
        if self.stack_1.size() == 0:
            return None
        if self.stack_2 is not None and self.stack_2.size() > 0:
            return self.stack_2.pop().value

        while self.stack_1.size() > 0:
            elem = self.stack_1.pop()
            if self.stack_2 is None:
                self.stack_2 = Stack(elem)
            else:
                self.stack_2.push(elem)
        return self.stack_2.pop().value


q = Queue(Element(1))
q.enqueue(Element(2))
q.enqueue(Element(3))
print(q.dequeue())
q.enqueue(Element(4))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(Element(5))
print(q.dequeue())