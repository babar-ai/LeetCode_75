'''
problem 151 (Reverse words in a string)

https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

Example:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        #step 1 --> reverse the string
        
        rev = s[::-1]
        N = len(rev) - 1
        i = 0
        result = ''
        
        
        while i < N:
            
            
            
            # Skip spaces
            while i < N and rev[i] == " ":
                i += 1
                
            word = ''
            
            #step 2 --> to find word
            
            while i <= N and rev[i] != " " :
                
                word += rev[i]
                i += 1
            
            if word:
                if result == "":
                    result = word[::-1]
                else:
                    result += " " + word[::-1]
                    
        return result
    



s = "  hello world "
S1 = Solution()
result = S1.reverseWords(s)
print(f'final result: {result}')



#clean and short solution 

def reverse_words(s):
    
    words = s.strip().split()
    words.reverse()
    
    return ' '.join(words)

result = reverse_words(" baber raheem")
print(result)