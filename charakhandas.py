
# https://www.prosperitynjoy.com/2015/04/vedic-astrology-charakhandas-and.html


from math import sin, radians,cos



print("""

1    :  Aeris
2    :  Taurus   
3    :  Gemini
4    :  Cancer
5    :  Leo
6    :  Virgo
7    :  Libra
8    :  Scorpio
9    :  Sagittarius
10   :  Caspricorn
11   :  Aquarius
12   :  Pisces


""")

first_set = ["1","6","7","12"]
second_set = ["2", "5", "8", "11"]

def get_chandrakhandas():

    zodiac = input("Enetr the relavent number: ")
    lat = radians(float(input("Enter the lattitude: ")))
    base = (19335312*sin(lat))/(cos(lat)*60)


    if zodiac in first_set:
        chandrakhandas = base*sin(radians(30))/(3365.3581)

    elif zodiac in second_set:
        chandrakhandas = base*sin(radians(60))/(7270.1068)

    else:
        chandrakhandas = base*sin(radians(90))/(20151)

    return chandrakhandas

if __name__ == "__main__":
    print(get_chandrakhandas())


