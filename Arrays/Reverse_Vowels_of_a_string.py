class Solution:
    def reverseVowels(self, s: str) -> str:
        String = []
        temp = [] #Temporary list for collecting vowels in it.
        temp_loc = []
        for i in range(len(s)):
            String.append(s[i])
        # print(String)
            if String[i] == 'a' or String[i] == 'e' or String[i] == 'i' or String[i] == 'o' or String[i] == 'u' or String[i] == 'U' or String[i] == 'A' or String[i] == 'E' or String[i] == 'I' or String[i] == 'O':
                    temp.append(s[i])
                    temp_loc.append(i)
        print(temp)
        print(f"Location{temp_loc}")
        temp.reverse()
        print(temp)
        for j in range(len(temp)):
             String[temp_loc[j]] = temp[j]
        return ''.join(String)
solution = Solution()
s = "aA"
print(solution.reverseVowels(s))




