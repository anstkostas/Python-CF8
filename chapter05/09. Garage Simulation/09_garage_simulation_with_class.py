from collections import deque

# A deque (“deck”) is a list-like container optimized for fast appends and pops from both ends.
# Why use a deque instead of a list?
# list.append() and list.pop() at the end are fast
# but operations at the left side (insert(0, x) / pop(0)) are slow (O(n))
# A deque gives you O(1) operations on both ends.
# 
# Common methods:
# d.append(x)        # add to the right
# d.appendleft(x)    # add to the left
# d.pop()            # remove from the right
# d.popleft()        # remove from the left
# d.extend(iterable)
# d.extendleft(iterable)
# d.rotate(n)        # rotate right (n>0) or left (n<0)

class Garage:
  def __init__(self, capacity):
    self.garage = deque()
    self.capacity = capacity

  def car_arrives(self, car):
    if len(self.garage) < self.capacity:
      self.garage.append(car)
      print(f"{car} arrived. Current stat of garage: {list(self.garage)}")
    else:
      print(f"{car} cannot arrive. Garage is full. Current state of garage: {list(self.garage)}")

  # Implements FIFO
  def car_leaves(self):
    if self.garage:
      car = self.garage.popleft()
      print(f"{car} left. Current state of garage: {list(self.garage)}")
      return car
    else:
      print("No cars in the garage to leave.")
      return None # Python returns None if no return statement provided.

  def find_car(self, car):
    if car in self.garage:
      position = list(self.garage).index(car) + 1 # Add 1 for UX(position 0 is bad UX)
      print(f"{car} is in the garage at position {position}")
    else:
      print(f"{car} is not in the garage")
  
def main():
  GARAGE_CAPACITY = 5
  garage = Garage(GARAGE_CAPACITY)

  # cars arriving simulation
  garage.car_arrives("Car 1")
  garage.car_arrives("Car 2")
  garage.car_arrives("Car 3")
  garage.car_arrives("Car 4")

  # car leaving the garage
  left_car_leaves = garage.car_leaves()
  print(left_car_leaves)

  garage.car_arrives("Car 5")
  garage.car_arrives("Car 6")
  garage.car_arrives("Car 7")

  garage.car_leaves()
  garage.car_leaves()
  garage.car_leaves()
  garage.car_leaves()
  garage.car_leaves()
  garage.car_leaves()
  garage.car_leaves()

if __name__ == "__main__":
  main()