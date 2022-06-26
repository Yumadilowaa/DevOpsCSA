print("Enter a line:")
line_origin = input('-> ')
count = {}
for i in line_origin.split():
    if i not in count:
        count[i] = 1
    else: 
        count[i] += 1
sorted_c = sorted(count.items(), key = lambda x: x[1], reverse = True)
max = sorted_c[0][1]
for i in sorted_c:
    if i[1] == max:
        print(i[0], ' - ', i[1])

    
