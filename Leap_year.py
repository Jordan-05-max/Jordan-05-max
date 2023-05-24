from pprint import pprint
year = 2024
leap = year % 4
leaps = year % 100
if leap == 0 and leaps != 0 or year % 400 == 0:
    pprint("Leap Year")
    print("leap year")
else:
    pprint("Not Leap Year")
    print("not leap year")