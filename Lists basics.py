x = [ "a" , "b", [3,3.5] , 4,]

print(x[0])
print(x[1])
print(x[2][1])
print(x[3])

x[1] = 2

print(x)
print(x * 3)

print("a" in x)
print(4 in x)

if "a" in x:
    print(x[1])
if 2 in x:
    print(x[3])

print(not 4 in x)
print(4 not in x)
print(1 not in x)

x.append(5)
print(x)
#add something to end of list

print(len(x))
#len gets number of items in list

index = 1
x.insert(index, "index")
print(x)
