# NOTE all methods with double underscores are overloaded and all with @ are decorated(extra functionality) with the name of the decorator.
class Point:
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def __str__(self):
    return f"({self.__x}, {self.__y})"
  
  def __add__(self, other):
    if isinstance(other, Point):  # isinstance receives two arguments, the object and the class it is.
      return Point(self.__x + other.__x, self.__y + other.__y)
    elif isinstance(other, (int, float)):
      return Point(self.__x + other, self.__y + other)
    else:
      raise TypeError("Unsupported operand types for +.")

  # Is the right-side version of the + operator. If a.__add__(b) returns NotImplemented then Python will try b.__add__(a).
  def __radd__(self, other):
    return self.__add__(other)

  def __eq__(self, other):
    if isinstance(other, Point):
      return self.__x == other.__x and self.__y == other.__y
    else:
      return False  # inferred


  @property
  def x(self):
    return self.__x
  
  @x.setter
  def x(self, value):
    self.__x = value

  @property
  def y(self):
    return self.__y
  
  @y.setter
  def y(self, value):
    self.__y = value

# Is a polymorphic function
# that bc for Point types __add__ is overloaded, so for p1 + p2 to be calculated the __add__ method of Point class is called
# otherwise would raise error, bc Python doesnt know how to add two instances of this class.
def my_add(a, b):
  return a + b

def main():
  p1 = Point(1, 2)
  p2 = Point(3, 4)

  print(my_add(10, 20))
  print(my_add(p1, p2))
  print(my_add(p1, 10))
  print(my_add("Hello", "CF8"))

  print("p1 + p2=", p1 + p2 )
  print("p1 + 10=", p1 + 10 )
  print("p1 + 10.5=", p1 + 10.5 )

  print("p1 == p2:", p1 == p2)
  print("p1 === 'Hello':", p1 == 'Hello')

  print("10 + p1=", 10 + p1)  # Without __radd__ this would raise error bc __add__ expects type Point for the first operand and the 2nd can be of int or double as well.

if __name__ == "__main__":
  main()