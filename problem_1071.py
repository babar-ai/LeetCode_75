"""
problem:  1071 greatest common divisor of strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
"""

import math

def gcdOfStrings(str1, str2):
    # Step 1: Check if a common pattern exists
    if str1 + str2 != str2 + str1:
        return ""
    
    # Step 2: Find the GCD of lengths
    gcd_length = math.gcd(len(str1), len(str2))
    
    # Step 3: Return the prefix of either string up to GCD length
    return str1[:gcd_length]

print(gcdOfStrings("abc", "abc"))
print(gcdOfStrings("leet", "code"))
