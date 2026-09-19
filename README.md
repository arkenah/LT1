# Circumference Calculator

## Computational Thinking

### Problem Identification
Calculate circumference and area of the garden, then calculate the square root, rounded down, and rounded up of the area

### Problem Decomposition
1. Get the radius
2. Calculate the area (A=2πr)
3. Use circumference formula (C=2πr)
4. Find square root of the area using math.sqrt
5. Determine rounded down area using math.floor
6. Determine rounded up area using math.ceil
7. Display results

### Pattern Recognition
Using math library functions for all calculations

### Data Representation
* Area and its rounded up and down represented in square meters
* Circumference represented in meters
* Square root represented with no unit

### Algorithm Development
* Function Main
    * Declare Float radius, circumference, square_root
    * Declare Integer area_rounded_down, area_rounded_up
  
    * Output "Enter radius of the garden in meters"
    * Input radius
    * area = 2πr
    * circumference = 2πr
    * square_root = math.sqrt(radius, 2)
    * rounded_down_area = math.floor(area)
    * rounded_up_area = math.ceil(area)
    * print(f"Area of the garden: {area:.2f} meters")
      * print(f"Circumference of the garden: {circumference:.2f} meters")
      * print(f"Square root of the area: {square_root:.2f} meters")
      * print(f"Area rounded down: {area_rounded_down} meters")
      * print(f"Area rounded up: {area_rounded_up} meters")


## Description
Asks for the radius of the circle, then calculates the circumference, area, square root, rounded down area, and rounded up area.

## How to Run
1. Open project file
2. Access the python file "CircularGarden.py"
3. Answer what is the radius
4. See the results

## Input Needed
* Radius

## Sample Output
* Input: 5
    * Area of the garden: 78.54 square meters
    * Circumference of the garden: 31.42 meters
    * Square root of the area: 8.86
    * Area rounded down: 78 square meters
    * Area rounded up: 79 square meters

## Author & Section
Author: Arkenah Mhyssy A. Salvador
Section: 8-Adelfa

