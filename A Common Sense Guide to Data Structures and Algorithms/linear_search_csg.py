"""
Linear Search implementation
src: A Common Sense Guide to Data Structures and Algorithms
"""


def linear_search(array, search_value):

    # Iterate through every element in the array
    for value in array:

        # If value is found return its index
        if value == search_value:
            return array.index(value)

    # If value not found return None
    return None


numbers = [1, 3, 2, 7, 9, 5]

print(linear_search(numbers, 3))
