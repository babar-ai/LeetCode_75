
def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxcandies = max(candies)
        
        return [c + extraCandies >= maxcandies for c in candies]

candies = [2,3,5,1,3]
extraCandies = 3

result1 = kidsWithCandies(candies, extraCandies)
print(result1)