def heapify(arr, n, i):
    largest = i  # Initialize the largest element as the root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if the left child exists and is greater than the root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if the right child exists and is greater than the current largest
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap the root (largest element) if needed and continue to heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap


# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", my_list)

heap_sort(my_list)

print("Sorted list:", my_list)
