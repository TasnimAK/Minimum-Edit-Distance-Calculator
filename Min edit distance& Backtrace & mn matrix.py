# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:44:30 2023

@author: Tasnim
"""

def min_edit_distance(str1, str2, substitution_cost=1):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + substitution_cost
                )

    # Printing the dp matrix
    for row in dp:
        print(row)

    i, j = m, n
    operations = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            operations.append(f"Match '{str1[i - 1]}'")
            i, j = i - 1, j - 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Delete '{str1[i - 1]}'")
            i -= 1
        elif dp[i][j] == dp[i][j - 1] + 1:
            operations.append(f"Insert '{str2[j - 1]}'")
            j -= 1
        else:
            operations.append(f"Substitute '{str1[i - 1]}' with '{str2[j - 1]}'")
            i, j = i - 1, j - 1

    while i > 0:
        operations.append(f"Delete '{str1[i - 1]}'")
        i -= 1
    while j > 0:
        operations.append(f"Insert '{str2[j - 1]}'")
        j -= 1

    operations.reverse()

    # Return the minimum edit distance and the list of edit operations.
    return dp[m][n], operations

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
substitution_cost = int(input("Enter the substitution cost (e.g., 2 for Levenshtein with cost 2): "))

distance, operations = min_edit_distance(str1, str2, substitution_cost)
print(f"Minimum Edit Distance: {distance}")
print("Edit Operations:")
for operation in operations:
    print(operation)
