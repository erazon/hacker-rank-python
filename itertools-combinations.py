from itertools import combinations


s, k = list(input().split())
s = ''.join(sorted(s))
for i in range(1, int(k)+1):
    print('\n'.join([''.join(j) for j in combinations(s, i)]))
