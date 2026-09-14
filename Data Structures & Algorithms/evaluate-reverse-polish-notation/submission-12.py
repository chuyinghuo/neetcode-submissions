class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for letter in tokens:
            if letter == "+":
                stack.append(stack.pop()+stack.pop())
            elif letter == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif letter == "*":
                stack.append(stack.pop()*stack.pop())
            elif letter == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(letter))
        return stack[0]
        