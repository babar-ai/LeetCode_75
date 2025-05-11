'''
#problem
https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

'''

def canPlaceFlowers(flowerbed, n):
    
    for i in range(len(flowerbed)):  # [1,0,0,0,1]
        
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                
                flowerbed[i] = 1
                
                n = n - 1
                if n==0:
                    return True
            
            
flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))
