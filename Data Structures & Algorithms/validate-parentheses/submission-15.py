class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = { '}': '{', ')': '(', ']': '['}
        stack = []

        for letter in s:
            if letter in "{([":
                stack.append(letter)
            elif letter in parentheses:
                if not stack or stack.pop() != parentheses[letter]:
                    return False 
        return not stack
        