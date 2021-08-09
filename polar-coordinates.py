import cmath
if __name__ == '__main__':
    complex_number = complex(input())
    print(*cmath.polar(complex_number), sep='\n')
