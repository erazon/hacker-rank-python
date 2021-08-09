def average(array):
    # your code goes here
    unique_set = set(array)
    return sum(unique_set)/len(unique_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
