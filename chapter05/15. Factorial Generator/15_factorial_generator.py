# The difference from iterator, is that I dont know in advance the number of iterations. Whenever the generator is called, the next() method is called and the next value is calculated. The generator haults its execution and remembers its state.
def facto():
    """
    Generator function to yield factorials indefinitely.
    
    Yields:
    int: The next factorial in the sequence.
    """
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n

def main():
    # Create a generator object for factorials
    f = facto()

    # Print the first 6 factorials (from 0! to 5!)
    for i in range(6):
        print(f"{i}! = {next(f)}")

    # Print the next 5 factorials (from 6! to 10!)
    for i in range(6, 11):
        print(f"{i}! = {next(f)}")

if __name__ == "__main__":
    main()
