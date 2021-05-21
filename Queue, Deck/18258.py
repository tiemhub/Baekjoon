#큐, 덱
#큐 2
import sys

queue = []

for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()
    if command == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        command, n = command.split()
        queue.append(int(n))
