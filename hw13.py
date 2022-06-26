def func(t, type):
    if type == "C":
        print(1.8 * t + 32, "F")
    elif type == "F":
        print((t - 32)/ 1.8, "C")

func(32, 'C')

