def wrapper(f):
    def fun(l):
        formatted = []
        for item in l:
            length = len(item)
            formatted.append("+91 "+item[length-10:length-5]+" "+item[length-5:])
        return f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
