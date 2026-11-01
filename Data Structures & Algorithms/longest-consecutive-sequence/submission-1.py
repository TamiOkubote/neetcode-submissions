class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences_in_set = set(nums)
        longest = 0
        for i in sequences_in_set: #for loop running through each item in list
            if (i - 1) not in sequences_in_set: #check if there is no number 1 smaller, hence validate if [i + 1] is greater to [i] by 1
                length = 1
                while (i + length) in sequences_in_set:
                    length = length + 1
                longest = max(longest, length) #choose what is longer - the current "longest" sequence ir the incremented length?
        return longest #return largest count
        