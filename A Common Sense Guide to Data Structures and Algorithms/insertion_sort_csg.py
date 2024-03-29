"""
Insertion Sort Implementation
src: A Common Sense Guide to Data Structures and Algorithms
"""


def insertion_sort(arr):
    for index in range(1, len(arr)):

        temp_value = arr[index]
        position = index - 1

        while position >= 0:
            if arr[position] > temp_value:
                arr[position + 1] = arr[position]
                position = position - 1
            else:
                break

        arr[position + 1] = temp_value

    return arr


numbers = [1, 3, 2, 7, 9, 5]

print(insertion_sort(numbers))