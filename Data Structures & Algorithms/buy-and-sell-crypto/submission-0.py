class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 0
        highest = 0
        bestProfit = 0

        for i in range(len(prices)):
            if i == 0:
                lowest = prices[i]
            else:
                if prices[i] < lowest:
                    lowest = prices[i]
                    #
                    highest = 0
                elif prices[i] > highest and prices[i] != lowest:
                    highest = prices[i]

                profit = highest - lowest
                if profit > bestProfit:
                    bestProfit = profit
        
        return bestProfit



