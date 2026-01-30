# Function and date structure
def calculate_area(length, width):
    """
    Function to calculate the area of a rectangle
    Parameters: length and width
    Returns: area of the rectangle
    """
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

result = calculate_area(length, width)

print(f"The area of the rectangle is: {result}")