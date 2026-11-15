class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence_in_set = set(nums)
        longest = 0
        for i in sequence_in_set:
            if (i - 1) not in sequence_in_set:
                length = 1
                while (i + length) in sequence_in_set:
                    length += 1
                longest = max(longest, length)
        return longest