from collections import defaultdict

if __name__ == '__main__':
    m, n = map(int, input().split())

    d = defaultdict(list)
    for i in range(m):
        d[input()].append(i+1)

    for i in range(n):
        print(*d[input()] or [-1])
