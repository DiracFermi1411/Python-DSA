class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        s = "".join(s)
        for i in range:
            s.remove(i)
            s.append(i)


s = ["h","e","l","l","o"]
solution = Solution()
print(solution.reverseString(s))