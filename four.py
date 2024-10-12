x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

# Determine the quadrant
if x == 0 and y == 0:
    print("The coordinate is at the origin.")
elif x > 0 and y > 0:
    print("The coordinate is in the first quadrant.")
elif x < 0 and y > 0:
    print("The coordinate is in the second quadrant.")
elif x < 0 and y < 0:
    print("The coordinate is in the third quadrant.")
elif x > 0 and y < 0:
    print("The coordinate is in the fourth quadrant.")

