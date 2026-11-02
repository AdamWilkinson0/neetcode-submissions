class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # attempt to sell at each r. keep track of minimums as go

        if len(prices) < 2:
            return 0

        l = 0
        r = 1

        lowest = prices[0]
        highest = 0
        

        while r < len(prices):
            if prices[r] - lowest > highest:
                highest = prices[r] - lowest
            
            if prices[r] < lowest:
                lowest = prices[r]
                l+=1
                r+=1
            else:
                r+=1

            

        return highest
            