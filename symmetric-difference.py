m, a = int(input()), set(map(int, input().split()))
n, b = int(input()), set(map(int, input().split()))

list_items = [*a.difference(b), *b.difference(a)]
list_items.sort()
for item in list_items:
    print(item)
