class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = n * [0]
        #(index, temperature)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                stack_i, stack_t = stack.pop()
                result[stack_i] = i - stack_i
            stack.append((i, t))
        return result

            


        