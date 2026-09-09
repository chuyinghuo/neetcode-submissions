class Solution:
    def isValid(self, s: str) -> bool:
        para = { ')':'(', '}': '{', ']':'['}

        stack = []

        for letter in s:
            if letter in '({[':
                stack.append(letter)
            elif letter in para:
                if not stack or stack.pop() != para[letter]:
                    return False 
        return not stack 
        