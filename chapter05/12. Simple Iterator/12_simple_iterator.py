class SimpleIterator:
    def __init__(self, data):
        """
        Initialize the iterator with the given data.
        To create an iterator I must implement 2 magic methods(__iter__, __next__).

        Parameters:
          data (list): The list of elements to iterate over.
        """
        self.data = data
        self.index = 0  # index of iterator

    def __iter__(self): # magic method
        """
        Return the iterator object itself.

        Returns:
          self (SimpleIterator): The iterator object itself.
        """
        return self

    def __next__(self): # magic method
        """
        Return the next item from the data. Raise StopIteration when the data is exhausted.

        Returns:
          int/float/str: The next item from the data.

        Raises:
          StopIteration: When there are no more items to return.
        """
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

def main():
    """
    Main function to demonstrate the usage of the SimpleIterator.
    """
    numbers = [10, 20, 30, 40, 50]

    # Create an instance of SimpleIterator
    iterator = SimpleIterator(numbers)

    # Use the iterator in a for loop
    for item in iterator:
        print(item)

if __name__ == "__main__":
    main()
