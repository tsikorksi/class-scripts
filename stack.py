import operator


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def pop(self):
        if Stack.is_empty(self):
            return None
        else:
            end = len(self.items)
            last = self.items[end]
            self.items.remove(last)
            return last

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if Stack.is_empty(self):
            return None
        else:
            end = len(self.items)
            last = self.items[end]
            return last


operators = {"+": operator.add, "-": operator.sub}

expression = input("Enter a post-fix arithmetic expression: e.g 2 2 +")

stack = Stack()
for word in expression.split():
    print(word)


# TASK: Complete the following tasks to build a Reverse Polish Notation Calculator

# 1. Add all required methods to the stack class
# 2. Add code to push operands onto the stack
# 3. Add code to pop off the necessary operands once an operator is found and then perform the operation
# on those operands (making use of the operators dictionary), outputting the result
# 4. Add resiliency so it handles erroneous input
