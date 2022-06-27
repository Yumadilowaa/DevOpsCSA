#problem 6
print(sum([i for i in range(1,101)])**2 - sum([i**2 for i in range(1,101)]))
#problem 9
print([b * a * ((1000 - a) - b) for b in range(1, 1001) for a in range(1, b) if a ** 2 + b ** 2 == ((1000 - a) - b) ** 2][0])
#problem 40
print(reduce(lambda x, y: x * y, [int(''.join([str(i) for i in range(200000)])[10**k]) for j in range(7)]))
#problem 48
print((str(sum([i**i for i in range(1,1001)])))[-10:])
