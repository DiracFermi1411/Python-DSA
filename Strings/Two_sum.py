class Solution:
    def twoSum(self, nums, target):

### Brute force soltuion with (On^2) ###
        # indices_list = []
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             # indices_list.append(i)
        #             # indices_list.append(j)

        #             return [i, j]

        # return []


### Using Hashmaps ###

        Hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in Hashmap:
                return [Hashmap[complement], i]
            
            Hashmap[num] = i

        return []
    
solution = Solution()
target = 6
nums = [3, 2, 4]
print(solution.twoSum(nums, target))
            
