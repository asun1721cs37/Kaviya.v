#leap year
def isLespYear(year):
  if (year%400==0 and year%100!=0)or year%400==0:
    return True
  else:
    return False

year=int(input("Enter the value:"))

if isLespYear(year):
    print ("{}is a leap year.". format (year))
else:
      print("{})is not a leap year.". formet (year))

