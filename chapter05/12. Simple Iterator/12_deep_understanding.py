# Μια λίστα από ακέραιους αριθμούς
numbers = [10, 20, 30, 40, 50, 60, 70]

# *** Why use iterators, instead of lists?? ***
# They are efficient ways of traversing data.
# For example, say I had a file of 1GB data and wanted to read the first 1 or 10.
# With the iterator to the cashed memory is loaded only what it is read, but with lists 
# all data must be loaded to traverse even the 1st line.
# 
# All iterators, generators implement build-in classes.
# Παίρνουμε έναν iterator από τη λίστα χρησιμοποιώντας τη συνάρτηση την build-in συνάρτηρη iter().
# Ένας iterator είναι ένα αντικείμενο που κρατά την "τρέχουσα θέση" και μπορεί να επιστρέφει τα στοιχεία ένα-ένα με next()
iterator = iter(numbers)  # iterator = SimpleIterator(numbers) -> Instead of build-in iter(), could use my custom iterator class.
print("Iterator object created.") 

# Προσομοιώνουμε τη συμπεριφορά ενός for-loop χρησιμοποιώντας while-loop και next()
# *** Η λογική πίσω από αυτό είναι να δούμε πώς λειτουργεί το for-loop εσωτερικά ***
while True:
    try:
        print("Calling next()...")  # Δηλώνει ότι θα καλέσουμε το next() στον iterator
        item = next(iterator)       # Επιστρέφει το επόμενο στοιχείο από τον iterator
        print("Got item:", item)    # Εμφανίζει το στοιχείο που λάβαμε

    except StopIteration:
        # Το next() όταν φτάσει στο τέλος της συλλογής προκαλεί την εξαίρεση StopIteration
        # Αυτό σηματοδοτεί το τέλος της ακολουθίας, όπως γίνεται και με ένα for-loop
        print("No more items. StopIteration raised.")
        break   # Βγαίνουμε από το βρόχο μόλις τελειώσουν τα στοιχεία
