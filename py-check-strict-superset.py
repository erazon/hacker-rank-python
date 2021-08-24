a = set(input().split())
result = True
for _ in range(int(input())):
    s = set(input().split())
    if not a.issuperset(s):
        result = False
print(result)
