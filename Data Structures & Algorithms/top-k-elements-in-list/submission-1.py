class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myDict = {}

        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]] = 1
            else:
                myDict[nums[i]] += 1
        #need to return keys with the highest values

        #sorted_by_value = dict(sorted(myDict.items(), key=lambda item: item[1]))
        

        return sorted(myDict, key=myDict.get, reverse=True)[:k]

