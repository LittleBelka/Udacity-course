from homework1and2.stack import Element, Stack

class Balance:
    def __init__(self, head=None):
        self.stack = Stack(head)

    def add(self, new_element):
        if self.stack.size() > 0 and self.stack.get_head() != new_element:
            self.stack.pop()
        else:
            self.stack.push(new_element)

    def check_balance(self):
        if self.stack.size() > 0:
            print("Balance isn't correct")
        else:
            print("Balance is correct")

string = "(aa(((d))rr)"
balance = Balance()
for i in string:
    if i == "(" or i == ")":
        balance.add(Element(i))
balance.check_balance()