class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialises empty dictionary, which will store key-value pairs
        store = {}
        #for loop to iterate through the list
        for i, num in enumerate(nums):
        #initialise complement to equal target - item
            complement = target - num
        #check that complement is in the dictionary
            if complement in store:
                return [store[complement], i] #returns indices
            store[num] = i
        