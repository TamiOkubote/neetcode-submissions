from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_words = tuple(sorted(word))
            anagrams[sorted_words].append(word)
        return list(anagrams.values())
        