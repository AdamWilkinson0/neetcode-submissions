class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProf = 0
        lowestVal = prices[0]

        for i in range(len(prices)):
            if prices[i] < lowestVal:
                lowestVal = prices[i]
            prof = prices[i] - lowestVal
            if prof > highestProf:
                highestProf = prof


        return highestProf



