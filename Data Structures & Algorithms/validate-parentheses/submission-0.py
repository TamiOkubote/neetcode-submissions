class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
            }
        #initialise variable to include opening charcaters
        opening_characters = "([{"
        #iterate through string s and store opening characters
        for character in s:
            if character in opening_characters:
                stack.append(character)
            elif character in pairs:
                if not stack or (stack[-1] != pairs[character]):
                    return False
                stack.pop()

        return len(stack) == 0