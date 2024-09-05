class Solution:
    def canPlaceFlowers(self, flowerbed:[int], n: int) -> bool:
        result = 0
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1 and flowerbed[i] == 0:
                result += 1
                return True
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        result += 1
                        flowerbed[i] = 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        result += 1
                        flowerbed[i] = 1
                elif (i > 0 and i < len(flowerbed)-1):
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        result = result + 1
                        flowerbed[i] = 1
        if result >= n:
            return True
        else:
            return False
flowerbed = [0,0,1,0,0]
n = 1
solution = Solution()
output = solution.canPlaceFlowers(flowerbed, n)
print(output)
