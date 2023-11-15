def knapsack_01(weights, values, capacity):
    n = len(weights)

    # Create a 2D table to store the maximum value for subproblems
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruct the selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], list(reversed(selected_items))

# Example usage:
weights = [4, 3, 2]
values = [5, 4, 3]
capacity = 5

max_value, selected_items = knapsack_01(weights, values, capacity)
print("Maximum Value:", max_value)
print("Selected Items:", selected_items)
