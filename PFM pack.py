seconds = 60
minutes = 60
secondsInHour = seconds * minutes

print("PFM for Pack")
x = int(input("Enter number of seconds Final station takes to complete part:"))
y = int(input("Enter number of seconds Pack station takes to complete part:"))
z = int(input("Time elapsed in minutes:"))

d = z * seconds
          
a = int(d / x)
b = int(d / y)
c = int(a - b)
print("After" , z ,"minutes, Final passes", a , "parts and pack passes" , b , "parts.")
print("This leaves WIP of" , c , "at pack")
