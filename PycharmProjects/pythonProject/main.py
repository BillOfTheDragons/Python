Radius = int(input("What is the radius of the circle you want to calculate the circumfrence of: "))
while Radius > 0:
    Diameter = float(Radius * 2)
    Pi = 3.14
    circumfrence = Diameter * Pi
    print("The value of circle you are looking for is: " + str(circumfrence))
    Area_variable = Radius * Radius * Pi
    print("By the way the area is: " + str(Area_variable))
    Radius = int(input("What is the radius of the circle you want to calculate the circumfrence of: "))