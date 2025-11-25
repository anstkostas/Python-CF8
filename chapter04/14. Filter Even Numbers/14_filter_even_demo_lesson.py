numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # ??? list(range(1, 11))

# filter(lambda x: x % 2 == 0, numbers) -> Creates a lazy iterator, does not filter yet.
# The anonymous function is called "predicate" | λογική συνθήκη
even_numbers_iterator = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_iterator) # <class 'filter'>
print(type(even_numbers_iterator)) # <class 'filter'>

for number in even_numbers_iterator:
  print(number, end=" ")
print()

print("--------------")

for number in even_numbers_iterator:
  print(number, end=" ")  # prints nth, why?? ** This is true when even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)
  # Bc even_numbers_iterator is an iterator, traverses the list, then when called here, there is no more "list" to traverse. 

  # Iterator characteristics ??
  # 1. produces items one by one
  # 2. does not store all results in memory
  # 3. can be consumed only once 
  # 
  # To overcome this wrap in a list -> list(filter(lambda x: x % 2 == 0, numbers)), 
  # Now the result of the iterator is stored in a list, which when called here whould display the same values [2, 4, 6, 8, 10].
print()

# for number in even_numbers_iterator:
#   if number == 4:
#     break
#   print(number, end=" ")  # 2
# print()

# print("--------------")

# for number in even_numbers_iterator:
#   print(number, end=" ")  # 6 8 10
# print()