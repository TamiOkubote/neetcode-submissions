class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #initialise empty dictionary of key-value pairs via letter-frequency
        string_S = {}
        string_T = {}
        #if statement to check lengths of two strings aren't the same
        if len(s) != len(t):
            return False
        #for loop to iterate through string
        for i in range(len(s)):
        #increment frquency by 1 as you iterate through the string to the dictionary
            string_S[s[i]] = string_S.get(s[i], 0) + 1
            string_T[t[i]] = string_T.get(t[i], 0) + 1
        #check to see if frequency of letters in string the same via the value of the dictionary
        return string_S == string_T