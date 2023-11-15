def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Return -1 if the target is not found in the list

# Example usage:
my_list = [1, 5, 8, 12, 23, 45, 56]
target_number = 23

result = binary_search(my_list, target_number)

if result != -1:
    print(f"The target number {target_number} is found at index {result}.")
else:
    print(f"The target number {target_number} is not found in the list.")
