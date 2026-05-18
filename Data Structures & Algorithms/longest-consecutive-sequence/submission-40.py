from collections import defaultdict 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        sequences = defaultdict(set)

        for n in sortedNums:
            if n-1 not in sortedNums:
                sequences[n].add(n)
                for k in sortedNums:
                    if k-1 in sequences[n]:
                        sequences[n].add(k)
       # print(sequences)
       
        sorted_seq = sorted(sequences.items(), key=lambda n: -len(n[1]))
        if sorted_seq == []:
            return 0 
        print(sorted_seq)
        sorted_len = [(len(n[1])) for n in sorted_seq]
        print(sorted_len)
        return sorted_len[0]
        