def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found

    return -1  # Return -1 if the target is not found in the list

# Example usage:
my_list = [12, 45, 7, 23, 56]
target_number = 7

result = linear_search(my_list, target_number)

if result != -1:
    print(f"The target number {target_number} is found at index {result}.")
else:
    print(f"The target number {target_number} is not found in the list.")
