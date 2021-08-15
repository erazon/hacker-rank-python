from itertools import combinations_with_replacement


s, k = input().split()
print('\n'.join([''.join(i) for i in combinations_with_replacement(''.join(sorted(s)), int(k))]))
