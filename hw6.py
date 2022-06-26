def palindromic(s):
    if str(s) == str(s)[::-1] and bin(s)[2:] == bin(s)[:1:-1]:
        return True
number = 0
for i in range(1, 1000000, 2):
    if palindromic(i):
        number += i
print(number)