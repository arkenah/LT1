import math

# Getting the radius from user to compute
radius = float(input("Enter radius of the garden in meters: "))

# Computing required calculations
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
square_root = math.sqrt(area)
area_rounded_down = math.floor(area)
area_rounded_up = math.ceil(area)

# Display Results
print(f"Area of the garden: {area:.2f} meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"Square root of the area: {square_root:.2f} meters")
print(f"Area rounded down: {area_rounded_down} meters")
print(f"Area rounded up: {area_rounded_up} meters")