print("Enter a line:")
line_origin = sorted(input('-> ').split())
for i in range(1, len(line_origin) - 1):
    if str(i) not in line_origin:
        print(i)
        exit()

