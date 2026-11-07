from collections import defaultdict #automatically creates an empty list for every new signature

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        #for loop to iterate through strs
        for word in strs:
            counts = [0] * 26 #count all 26 lowercase English letters
            for character in word:
                index = ord(character) - ord("a") #method to find out index of each letter in alphabet
                counts[index] += 1 #increment count of character by 1 based off their index
        #strings with the same letter-frequency pairs would be grouped
            signature = tuple(counts)
            store[signature].append(word)
        return list(store.values()) #return the grouped strings as a list of lists