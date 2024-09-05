class Solution:
    def gcdOfStrings(str1, str2):
        len1, len2 = len(str1), len(str2)
        result = ""

        for i in range(min(len1, len2)):
            if str1[i] != str2[i]:
                break
            result += str1[i]
            if len1 % len(result) == 0 and len2 % len(result) == 0:
                if result * (len1 // len(result)) == str1 and result * (len2 // len(result)) == str2:
                    return result

        return ""

str1 = "AB"
str2 = "ABABAB"    
solution = Solution()
output = Solution.gcdOfStrings(str1, str2)
print(output)

