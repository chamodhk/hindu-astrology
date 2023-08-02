#let's calculate ayanamsa
#all the equations are based on the book of B.V. Raman.

year = int(input("Enter the year: "))

def calculate(year):
  ayanamsa = (year - 397)*151/3
  minutes = int(ayanamsa/3600)
  seconds = int((ayanamsa - (minutes*3600))/60)
  milli_seconds = int(ayanamsa - (minutes*3600))%60
  
  return minutes,seconds, milli_seconds


min, sec, mil = calculate(year)

print(f"{min} * {sec}' {mil}''")
