from math import sqrt

# Function to calculate distance between two points
def OD(x1, y1, x2, y2):
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("================================================")
    print('Distance:', distance)
    print("================================================")

# Function to check if a string contains any letters
def has_letter(value):
    # Returns True if any character in the string is an alphabet letter
    return any(ch.isalpha() for ch in value)

# Main input loop
while True:
    print("================================================")
    x1 = input("Enter x of point 1: ")
    y1 = input("Enter y of point 1: ")
    x2 = input("Enter x of point 2: ")
    y2 = input("Enter y of point 2: ")
    print("================================================")
    print("1th point : (", x1, ",", y1, ")")
    print("2th point : (", x2, ",", y2, ")")

    # Check if any of the inputs contain letters
    if has_letter(x1) or has_letter(y1) or has_letter(x2) or has_letter(y2):
        print("Try again. Please enter numbers only.\n")
        print("================================================")
        continue
    try:
        # Convert all inputs to integers
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    except ValueError:
        # Handle cases where the input cannot be converted to an integer
        print("Invalid input. Try again.\n")
        print("================================================")
        continue
    else:
        # Call the distance function and exit the loop
        OD(x1, y1, x2, y2)
        break