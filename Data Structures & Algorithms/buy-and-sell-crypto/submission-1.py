class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProf = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > highestProf:
                    highestProf = prices[j]-prices[i]





        return highestProf



