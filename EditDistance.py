def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store the minimum edit distances
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the table for base cases
    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    # Fill in the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j],         # Deletion
                                      table[i][j - 1],         # Insertion
                                      table[i - 1][j - 1])     # Substitution

    # The bottom-right cell contains the edit distance
    return table[m][n]

# Example usage:
str1 = "kitten"
str2 = "sitting"

result = edit_distance(str1, str2)

print(f"The Edit Distance between '{str1}' and '{str2}' is: {result}")
