''''
https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

345: Reverse the Vowels of string

'''

def reverseVowels(s):
    
    s_list = list(s)
    
    Left, Right = 0, len(s_list) - 1
    
    vowels = set('aeiouAEIOU')
    
    while Left < Right:
        
        while Left < Right and s_list[Left] not in vowels:
            Left += 1
        
        while Left < Right and s_list[Right] not in vowels:
            Right -= 1
            
            
        s_list[Right], s_list[Left] = s_list[Left], s_list[Right]
        Left += 1
        Right -= 1
    
    return ''.join(s_list)

s = "leetcode"
# leotcede
# vowels : a,e,i,o,u
resualtan = reverseVowels(s)
print(s)
print(resualtan)
