class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        f1 = []
        if len(s) == 1:
            return s
        else:
            for i in range(length):
                for j in range((length-1), -1, -1):
                     while i != j:
                         if s[i] == s[j]:
                             f1.append(s[i])
                         else:
                             f1 = []
                     continue
        return f1

s = "baddab"                  
solution = Solution()
print(solution.longestPalindrome(s))



 
