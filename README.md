# Longest Substring Without Repeating Characters

This is a beginner-level Python program that finds the **length of the longest substring without repeating characters** from a given string.

# What the Program Does

It checks every character in the input string and keeps track of the current substring without repeated characters.  
When a duplicate is found, it adjusts the substring accordingly and continues until the longest possible unique substring is found.

# Example Inputs and Outputs
print(length_of_longest_substring("bcbbb"))      # ➜ 2
print(length_of_longest_substring("pwwkew"))     # ➜ 3
print(length_of_longest_substring("abcabcbb"))   # ➜ 3
print(length_of_longest_substring("dvdf"))       # ➜ 3
print(length_of_longest_substring("aab"))        # ➜ 2
print(length_of_longest_substring("tmmzuxt"))    # ➜ 5

 Expected Output
2
3
3
3
2
5

 How It Works
A temporary string (current) is used to build substrings without duplicates.

When a duplicate character is found, the substring is sliced to remove the earlier duplicate.

It updates the longest value if a longer substring is found.

 How to Run
Make sure Python is installed:
Run python3 --version in terminal to check.

Run the script in your terminal:


python3 longest_substring.py

 Files
longest_substring.py — Main Python file containing the code
README.md — This file

 Author,
Beryl Nyambeki.
