class Solution:
    def threeSum(self, numbers: List[int]) -> List[int]:
        #three indexes must add up to 0 
        numbers.sort()

        final = []

        for index, value in enumerate(numbers):
            
            if numbers[index] > 0:
                break
            if index > 0 and value == numbers[index-1]:
                continue  
        # index + left + right = 0 
            left = index+1
            right = len(numbers)-1
            while left < right:
                if numbers[index] + numbers[left] + numbers[right] < 0:
                    left += 1 
                elif numbers[index] + numbers[left] + numbers[right] > 0:
                    right -= 1
                else:
                    final.append([numbers[index], numbers[left], numbers[right]])
                    left += 1
                    right -= 1 
                    
                    while numbers[left] == numbers[left-1] and left < right:
                        left += 1 
        return final

