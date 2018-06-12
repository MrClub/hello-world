seconds = 60
minutes = 60
hours = 24
year = 365

secondsInDay = hours * minutes * seconds
secondsInYear = year * secondsInDay

print("Total number of babies born every second over years")

x = (int(input("Enter a number of years: ")))
y = (int(input("Number of seconds: ")))
year = secondsInYear * x
births = int(year / y )


print("If a birth every ", y , "seconds, in " , x , "years: " , births, "babies born")
