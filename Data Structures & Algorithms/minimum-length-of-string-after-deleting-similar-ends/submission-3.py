class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0 
        r = len(s)-1

        while l < r and s[l] == s[r]:
            curr = s[l]
            while l + 1 < r and s[l+1] == s[r]:
                l += 1 
            while l < r-1 and s[r-1] == s[l]:
                r -= 1 
            l += 1 
            r -= 1
        return max(r-l+1, 0)

        

                







