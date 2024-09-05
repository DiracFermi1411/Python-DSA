class Solution:
    def groupAnagrams(self, strs):

        # if not strs:
        #     return strs
        # elif len(strs) == 1 and len(strs)[0] == 1:
        #     return strs
        
        # if len(strs)>1:
        #     for i in range(len(strs)):
        #         sorted_list = ''.join(sorted(strs))
        
        anagrams = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(str)
        
        return list(anagrams.values())
            

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs))