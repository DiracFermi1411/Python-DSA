class Solution:
    def isSubsequence(self, s, t):
        sPtr, tPtr = 0, 0  # Initialize pointers for both strings

        while sPtr < len(s) and tPtr < len(t):
            if s[sPtr] == t[tPtr]:
                sPtr += 1  # Increment the s pointer
            tPtr += 1  # Always increment the t pointer

        # If sPtr reached the end of s, it's a subsequence
        return sPtr == len(s)
solution = Solution()
# Example usage:
s1 = "abc"
t1 = "ahbgdc"
print(solution.isSubsequence(s1, t1))  # Output: True

s2 = "axc"
t2 = "ahbgdc"
print(solution.isSubsequence(s2, t2))  # Output: False
