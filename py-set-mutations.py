_, s = input(), set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    getattr(s, command[0])(set(map(int, input().split())))
print(sum(s))
