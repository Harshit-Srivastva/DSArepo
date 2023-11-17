def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store the lengths of common suffixes
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of the longest common substring
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1

                # Update the length and ending index of the longest common substring
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index = i - 1
            else:
                table[i][j] = 0

    # Extract the longest common substring from the input strings
    common_substring = str1[end_index - max_length + 1:end_index + 1]

    return common_substring

# Example usage:
str1 = "ABABC"
str2 = "BABCAC"

result = longest_common_substring(str1, str2)

print(f"The Longest Common Substring of '{str1}' and '{str2}' is: '{result}'")
