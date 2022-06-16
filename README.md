# Palindromes
This is a function where a number is taken in as a parameter argument and then returns True or False whether the number is a palindrome.
The challenge was to do it without changing the number into a string.
To do this, I used arithmetic and mod to separate each digit. Then I placed each individual digit into a list where later it can be compared to see 
if it is the same number in reverse format.

LeetCode Challenge:
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
Constraints:
-231 <= x <= 231 - 1
