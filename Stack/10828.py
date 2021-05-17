#Stack
#스택 구현
import sys

class stack():
    value = []
    def __init__(self):
        pass

    def push(self,n):
        self.value.append(n)

    def pop(self):
        if len(self.value) != 0:
            return self.value.pop()
        else:
            return -1

    def size(self):
        return len(self.value)

    def empty(self):
        if len(self.value) != 0:
            return 0
        else:
            return 1

    def top(self):
        if len(self.value) != 0:
            return self.value[-1]
        else:
            return -1


mystack = stack()
for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()
    if command == 'top':
        print(mystack.top())
    elif command == 'size':
        print(mystack.size())
    elif command == 'empty':
        print(mystack.empty())
    elif command == 'pop':
        print(mystack.pop())
    else:
        command, n = command.split()
        mystack.push(int(n))
