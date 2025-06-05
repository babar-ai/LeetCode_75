'''
  238. Product of Array Except Self
  https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75
  
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
  
'''

# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
    
#         result = []
        
#         for i in range(len(nums)):
#             prod = 1
            
#             for j in range(len(nums)):
#                 if i != j:
#                     prod *= nums[j]
                    
#             result.append(prod)

#         return result
    
    
# nums = [1,2,3,4]
# S1 = Solution()
# result = S1.productExceptSelf(nums)
# print("hello")
# print(result)




#Optimal Approch
"""
 Quick Notes: Product of Array Except Self
No division, O(n) time.

Use prefix and suffix products.

First pass: store prefix in result.

Second pass: multiply by suffix (right to left).

Initialize result with [1] * n.

Time: O(n), Space: O(1) extra.


"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        #we have to calculate prefix and suffix for each digit in array
        
        
        prefix = 1
        n = len(nums)
        result = [1] * n
        
        for i in range(n):
            
            result[i] = prefix
            prefix *= nums[i]
        

        #suffix
        suffix = 1
        
        for i in range(n-1, -1, -1):      #reverse loop
            
            result[i] *= suffix
            suffix *= nums[i]
            
            
        return result
    
nums = [1,2,3,4]
S1 = Solution()
result = S1.productExceptSelf(nums)
print(result)
