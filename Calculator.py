print("Basic Calculator")
symbols = [ "+", "-" , "*" , "/" , "quit"]



while True:
    x = input("Enter a number: ")
    if x == symbols[4]:
        break
    else:
        float(x)
    y = input("Add + , subtract - , multiply * , divide / or quit? ")
    if y not in symbols:
        print("Error")
        continue
    z = float(input("Enter a number: "))

    if y == symbols[4]:
        break
    elif y == symbols[0]:
        a = x + z
        print(a)
    elif y == symbols[1]:
        a = x - z
        print(a)
    elif y == symbols[2]:
        a = x * z
        print(a)
    elif y == symbols[3]:
        a = x / z
        print(a)
    
print("Program End")    
    

