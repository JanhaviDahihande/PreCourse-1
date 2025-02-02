class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.last = None
    def push(self, data):
        node = Node(data)
        if self.last == None:
            self.last = node
        else:
            node.next = self.last
            self.last = node 
    def pop(self):
        if self.last is None:
            return None
        else:
            data = self.last.data
            self.last = self.last.next
            return data
        
a_stack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
