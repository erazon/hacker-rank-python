import re
for _ in range(int(input())):
	x, y = input().split()
	m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
    	print(x,y)
