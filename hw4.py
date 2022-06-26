import re
print("Enter a line:")
line_origin = input('-> ')
print(sum([int(n) for n in re.findall(r'-?\d+', line_origin)]))