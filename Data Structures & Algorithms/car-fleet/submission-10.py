class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #target 10 
        #position 1, speed 3
        #postion 4, speed 2 

        #position 10-1 = 9; 9/3 = 3 (3 units to get to target)
        #position 10-4 = 6; 6/2 = 3 (3 units to get to target)
        #becomes a car flet 

        car_fleet = 0
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        for p, s in pair:
            time = (target-p)/s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() 
        return len(stack)
        



