import numpy


n = int(input().split()[0])
num_arr = []
for _ in range(n):
    num_arr.append(list(map(int, input().split())))
my_arr = numpy.array(num_arr)
print(numpy.transpose(my_arr))
print(my_arr.flatten())
