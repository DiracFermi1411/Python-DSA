class Solution:
    def isPalindrome(self, s):

        ### <output expression> for <variable> in <iterable> if <condition> ###
        cleaned_s = ''.join(char for char in s if char.isalnum()).lower()

        # print(cleaned_s)
        

        return cleaned_s == cleaned_s[::-1]
    
solution = Solution()
s = "0P"
print(solution.isPalindrome(s))

