
print("Enter a line:")
line_origin = input('-> ')
words = line_origin.split()
def get_unique(line):
    unique = []
    for u in line:
        if u not in unique:
            unique.append(u)
    print(" ".join(unique))
get_unique(words)