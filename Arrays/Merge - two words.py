class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(f"This is the lenght of {word1}: {len(word1)}")
        print(f"This is the lenght of {word2}: {len(word2)}")
        final_list = []
        if len(word1) > len(word2):
            for i in range(len(word2)):
                final_list.append(word1[i])
                final_list.append(word2[i])
            final_list.append(word1[len(word2):])
            print("".join(final_list))
        elif len(word2)> len(word1):
            for i in range(len(word1)):
                final_list.append(word1[i])
                final_list.append(word2[i])
            final_list.append(word2[len(word1):])
            print("".join(final_list))
        else:
            for i in range(len(word1)):
                final_list.append(word1[i])
                final_list.append(word2[i])
            print("".join(final_list))
    





word1 = "anti-"
word2 = "mouse"
solution = Solution()
output = solution.mergeAlternately(word1=word1, word2=word2)
