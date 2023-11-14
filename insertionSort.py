def insertion_sort(arr):
    # Traverse through all array elements starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be compared and inserted into the sorted sequence
        j = i - 1  # Index of the last element in the sorted sequence

        # Move elements of the sorted sequence that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position in the sorted sequence
        arr[j + 1] = key

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", my_list)

insertion_sort(my_list)

print("Sorted list:", my_list)
