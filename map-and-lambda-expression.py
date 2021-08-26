cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    fib_series = [0,1]
    for i in range(2,n):
        fib_series.append(fib_series[i-2] + fib_series[i-1])
    return fib_series


if __name__ == '__main__':
