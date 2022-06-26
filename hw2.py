def get_unique(line):
    unique = []
    for u in line:
        if u not in unique:
            unique.append(u)
    print(" ".join(unique))
print("Enter a line:")
line_origin = input('-> ')
words = line_origin.split()
get_unique(words)