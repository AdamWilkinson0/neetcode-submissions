class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
# [1,9] -> [,0]

        for i in range(len(digits)-1,-1,-1):
            
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                
                #digits[i-1] += 1
                
            #if digits[i-1] != 9:
                #break
        digits.insert(0, 1)
        return digits