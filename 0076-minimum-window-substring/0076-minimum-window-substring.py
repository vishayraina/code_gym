class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(hmap,tmap):
            for c in tmap:
                if tmap[c] > hmap.get(c, 0):
                    return False
            return True
    
        tmap = {}
        hmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        l = 0
        res, sol = float("inf"), [0,0]
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            while is_valid(hmap, tmap):
                if res > r-l+1:
                    res = r-l+1
                    sol[0] = l
                    sol[1] = r+1
                hmap[s[l]] -= 1
                l += 1
        return s[sol[0]: sol[1]]

