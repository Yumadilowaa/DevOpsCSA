print("Enter a number:")
n = int(input('-> '))
a, b = 1, 1
print(a, b, end = " ")
for i in range(2, n):
    a, b = b, a + b
    print(b, end = " ")
