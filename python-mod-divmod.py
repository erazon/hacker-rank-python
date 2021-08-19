a, b = int(input()), int(input())
c = divmod(a, b)
print('\n'.join(list(map(str, [c[0], c[1], c]))))
