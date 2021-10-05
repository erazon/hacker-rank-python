import re
for _ in range(int(input())):
	for m in re.findall(r'(#(?:[\da-fA-F]{3}){1,2})[^\n ]', input()):
		print(m)