import re
def toint(str):
    if re.search(r'\D', str):
        return False
    if (len(str) == 1):
        return ord(str[0]) - ord('0')
    y = toint(str[1:])
    x = ord(str[0]) - ord('0')
    x = x * (10**(len(str) - 1)) + y
    return x
def main():
    print("Enter a line:")
    line_origin = input('-> ')
    if line_origin == 'cancel':
        print("Bye!")
        exit()
    else: 
        number = toint(line_origin)
        if number== False:
            print("Не удалось преобразовать введенный текст в число.")
        elif number % 2 == 0:
            print(number // 2)
        else:
            print(number * 3 + 1)
    main()

main()



