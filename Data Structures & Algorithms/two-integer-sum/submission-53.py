
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        index_map = {}
        for index, value in enumerate(nums):
            index_map[value] = index

        for index, value in enumerate(nums):
            difference = target - value
            if difference in index_map and index_map[difference] != index:
                return [index, index_map[difference]]
            else:
                index_map[value] = index


        