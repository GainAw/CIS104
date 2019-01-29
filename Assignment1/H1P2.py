print("Please enter in the number of miles you wish to convert: ")
miles = int(input())
kilometers = miles * 1.609
if(miles <= 1):
    print("{} mile is equal to {} kilometers".format(miles, kilometers))
else:
    print("{} miles is equal to {} kilometers".format(miles, kilometers))