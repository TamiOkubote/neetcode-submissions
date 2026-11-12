class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            string = str(len(word)) + "#" + str(word)
            encoded_string += string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        # Keep processing while i is within the encoded string
        while i < len(s):
        # Find the next '#' delimiter
            j = i
            while s[j] != "#":
                j += 1
        # Extract the string length
            length = int(s[i:j])
        # Extract the original string
            word = (s[j + 1:j + 1 + length])
        # Append it to result and update i
            result.append(word)
            i = j + 1 + length
        return result