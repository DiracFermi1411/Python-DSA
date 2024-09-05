class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_list = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_list.append(0)
        # print(zeros_list)
        for i in range(len(zeros_list)):
            nums.remove(0)
            nums.append(0)
        print(nums)
nums = [0,1,0,3,12]
solution = Solution()
output = solution.moveZeroes(nums)
print(output)
