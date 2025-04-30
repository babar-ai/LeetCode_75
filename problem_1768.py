# problem 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75


# FIRST APPROCH 

def mergeAlternately(word1, word2) -> str:
    
    new_str = ""
    i = 0
    
    while i < max(len(word1), len(word2)):
        
        if i < len(word1):
            new_str += word1[i]
            
        
        if i < len(word2):
            new_str += word2[i]
        
        i += 1
        
    return new_str
        
 
word1 = "ab"
word2 = "cde"
merge_str = mergeAlternately(word1, word2)
print(merge_str)
        
    

        

    