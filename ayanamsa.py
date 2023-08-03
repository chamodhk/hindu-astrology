#let's calculate ayanamsa
#all the equations are based on the book of B.V. Raman.

year = int(input("Enter the year: "))

def calculate(year):
  ayanamsa = (year - 397)*151/3
  degrees = int(ayanamsa/3600)
  minutes = int((ayanamsa - (minutes*3600))/60)
  seconds = int(ayanamsa - (minutes*3600))%60
  
  return degrees,minutes, seconds


deg,min, sec = calculate(year)

print(f"{deg} * {min}' {sec}''")
