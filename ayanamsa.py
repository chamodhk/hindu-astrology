#every year vernal equinox shift to west as a result of preseccion of equinoxes
# with this script you can calculate how it has been moved 

year = int(input("Enter the year: "))

def calculate(year):
  ayanamsa = (year - 397)*151/3
  degrees = int(ayanamsa/3600)
  minutes = int((ayanamsa - (degrees*3600))/60)
  seconds = int(ayanamsa - (degrees*3600))%60
  
  return degrees,minutes, seconds


deg,min, sec = calculate(year)

print(f"{deg} * {min}' {sec}''")
