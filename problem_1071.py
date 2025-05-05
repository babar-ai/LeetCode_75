"""
problem:  1071 greatest common divisor of strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
"""

def gcdOfStrings(str1, str2):
    
    length1 = len(str1)
    length2 = len(str2)
   

    def IsDivisor(l):
        if length1 % l or length2 % l:          # if 0 or 0: the funtion continouse does'nt return anything as it false becouse of both zeros
            return False
        
        f1, f2 = length1 // l, length2 // l
        
        return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
    
    for l in range(min(length1, length2), 0, -1):
        if IsDivisor(l):
            return str1[:l]
        
    return " "


str1 = "ABABAB"
str2 = "ABAB"
gcd = gcdOfStrings(str1, str2)
print(gcd)




'''
 Key Note for Future:
✅ In gcdOfStrings(), we try all possible prefix lengths (from largest to smallest) that could divide both strings' lengths.
✅ We check if repeating that prefix exactly rebuilds both strings.
❌ If the length l doesn’t evenly divide both str1 and str2, we skip it immediately.

🧠 Bonus tip (write in your notes):
🧩 str1[:l] is the candidate pattern, and str1[:l] * (length1 // l) must equal str1. Same for str2.
This confirms that the pattern repeats perfectly to form both strings.

'''