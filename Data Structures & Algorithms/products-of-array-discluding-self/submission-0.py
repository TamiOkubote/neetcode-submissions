class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        #for loop to iterate through list
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        #calculation to ouput the product of all elements in list
        #if statement to exlude nums[i] in calculation 
        return result #return output list that contains the product for each index
        