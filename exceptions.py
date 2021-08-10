# need to run with python2
if __name__ == '__main__':
    test_cases = int(raw_input())

    for i in range(test_cases):
        try:
            a, b = map(int, raw_input().split())
            print(int(a/b))
        except (ValueError, ZeroDivisionError) as e:
            print 'Error Code:', e