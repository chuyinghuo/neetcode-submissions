from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_t = Counter(t)
        window = Counter()
        matched_char = 0
        min_start = -1
        min_length = float('inf')

        l = 0 

        for right, char in enumerate(s):
            window[char] += 1 
            if char in target_t and window[char] <= target_t[char]:
                matched_char +=1

            while matched_char == len(t):
                curr_length = right - l + 1
                if curr_length < min_length:
                    min_start = l
                    min_length = curr_length
                
                s_left = s[l]
                if s_left in target_t and target_t[s_left] >= window[s_left]:
                    matched_char -= 1
                window[s_left] -=1
                l +=1 
        return '' if min_start == -1 else s[min_start: min_start+min_length]





