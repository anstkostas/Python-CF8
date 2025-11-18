num1 = 100

def my_add_function(a, b):
  return a + b

def main():
  print(f"Value of num1 is {num1}")
  print(my_add_function(1, 2))
  print(__name__) # When this is executed form another file, will print my_calculations.py

main()

# main() will be executed only when this file is executed directly "python my_calculations.py"
# if __name__ == "__main__":
#   main()