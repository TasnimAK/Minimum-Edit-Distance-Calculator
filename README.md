# Minimum-Edit-Distance-Calculator
"A Python tool for calculating the minimum number of edits required to convert one string into another, with customizable substitution costs."


This repository contains a Python script for computing the Minimum Edit Distance between two strings. The algorithm utilizes dynamic programming to determine the least costly sequence of edit operations—insertions, deletions, and substitutions—that transform one string into another. It is capable of handling customizable substitution costs, making it adaptable for variations of the problem, such as the Levenshtein distance, where substitution cost may differ from the default value of 1. 

The repository includes:
- Implementation of the Minimum Edit Distance algorithm.
- Backtracking to retrieve the actual edit operations.
- User interaction for input strings and substitution cost.

The output of the script is the minimum edit distance and a list of the specific edit operations required to transform the input string `str1` into `str2`.
