def is_square(length: float, width: float) -> bool:
    """
    Checks if a rectangle is a square.

    Args:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    bool: True if the rectangle is a square, False otherwise.
    """
    return length == width

def main():
    # Get user input for the length and width of the rectangle
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers for length and width.")
        return

    # Check if the rectangle is a square and print the result
    if is_square(length, width):
        print("The rectangle is a square.")
    else:
        print("The rectangle is not a square.")

if __name__ == "__main__":
    main()
