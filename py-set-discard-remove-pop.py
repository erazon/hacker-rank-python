input()
s = set(map(int, input().split()))
for _ in range(int(input())):
    command = input().split()
    try:
        if command[0] == 'pop':
            s.pop()
        if command[0] == 'remove':
            s.remove(int(command[1]))
        if command[0] == 'discard':
            s.discard(int(command[1]))
    except KeyError:
        pass
print(sum(s))
