def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # If the array has 0 or 1 element, it's already sorted

    pivot = arr[len(arr) // 2]  # Choose the pivot as the middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", my_list)

my_list = quick_sort(my_list)

print("Sorted list:", my_list)
