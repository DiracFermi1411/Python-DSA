class Solution:
    def kidsWithCandies(self, candies:[int], extraCandies: int) -> [bool]:
        results = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                results.append(True)
            else:
                results.append(False)
        return results

candies = [12,1,12] 
extraCandies = 10
solution = Solution()
output = solution.kidsWithCandies(candies, extraCandies)
print(output)
