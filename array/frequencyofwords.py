def frequency():
    n = input("Enter a string: ")
    dt = {}
    for i in n:
        if i in dt:
            dt[i] +=1
        else:
            dt[i] = 1

    print("count of all the letters in the string", str(dt))

frequency()
