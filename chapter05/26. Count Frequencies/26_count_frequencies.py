from collections import Counter
# Shows different ways of calculating frequencies of elements in a list.
def count_with_dict_comprehension(my_list: list[int]):
    """
    Count frequencies using dictionary comprehension. 
    NOTE converts list to set bc with list however many times an item is
    in the list, that many times its frequency will be calculated BUT its
    frequency will be stored only one time. So by converting to a set the
    function searches for the unique items only.
    """
    # return {item: my_list.count(item) for item in my_list}
    frequency_dict = {item: my_list.count(item) for item in set(my_list)}
    print("\nDictionary Comprehension:", frequency_dict)

def count_with_manual_loop(my_list: list[int]):
    """
    Count frequencies using a manual loop and conditional check.
    Calculates the same thing as the previous.
    """
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    print("\nManual Loop:", frequency_dict)

def count_with_get_method(my_list):
    """
    Count frequencies using a manual loop with `get()` method for default values.
    Increment the frequency of an item found in the frequency_dict. If not found
    default to 0.
    """
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1  # At the item of dictionary with key == item get its value or 0 if not found and add 1.
    print("\nManual Loop with get():", frequency_dict)  # Manual Loop with get(): {'apple': 3, 'banana': 2, 'kiwi': 4, 'orange': 1, 'melon': 1}

def count_with_counter(my_list):
    """
    Count frequencies using `Counter` from the `collections` module.
    """
    frequency_dict = Counter(my_list)
    print("\nUsing Counter:", frequency_dict) # Using Counter: Counter({'kiwi': 4, 'apple': 3, 'banana': 2, 'orange': 1, 'melon': 1})
    # Get elements sorted by frequency
    sorted_by_freq = frequency_dict.most_common() # Adding [:3] returns the first three!
    print("\nSorted by Frequency:", sorted_by_freq) # Sorted by Frequency: [('kiwi', 4), ('apple', 3), ('banana', 2), ('orange', 1), ('melon', 1)]

def main():
    # Original list of strings
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]

    # Demonstrate different ways to count frequencies
    count_with_dict_comprehension(my_list)
    count_with_manual_loop(my_list)
    count_with_get_method(my_list)
    count_with_counter(my_list)

if __name__ == "__main__":
    main()
