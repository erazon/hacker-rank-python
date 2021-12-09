import numpy


n, m, p = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(list(map(int, input().split())))
array_1 = numpy.array(num_list)

num_list = []
for _ in range(m):
    num_list.append(list(map(int, input().split())))
array_2 = numpy.array(num_list)

print(numpy.concatenate((array_1, array_2), axis=0))
