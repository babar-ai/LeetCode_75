class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) 
        first = float('inf')
        second = float('inf')
                                             
        for num in nums:
            
            if num <= first:
                first = num
                
            elif num <= second:
                second = num

            else :
                return True
            
            return False
            
            
            
            
nums = [2,1,5,0,7,6] 
S1 = Solution()
print(f'{S1.increasingTriplet(nums) }')          
                