class Solution:
    def containsDuplicate(self, nums):

        n = len(nums)
        hash = set()

        for i in range(n):

            if nums[i] in hash:
                return True
            hash.add(nums[i])

        return False
            
nums = [1,1,1,3,3,4,3,2,4,2]
solution = Solution()
output = solution.containsDuplicate(nums=nums)
print(output)