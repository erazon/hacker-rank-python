from collections import deque
d = deque()
for _ in range(int(input())):
    command = input().split()
    getattr(d, command[0])(*command[1] if len(command)>1 else [])
print(' '.join(map(str, d)))
