class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        indicies = defaultdict(int)

        
        for i in range(len(numbers)):
            indicies[numbers[i]] = i 
        print(indicies)
        
        for j in range(len(numbers)):
            if target - numbers[j] in indicies:
                num2 = target - numbers[j]
                res.append(j+1)
                res.append(indicies[num2]+1)
                return list(res)
            
            

        