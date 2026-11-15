class Solution:
    def secondHighest(self, s: str) -> int:
        l = []
        for i in s:
            if i.isdigit() and i not  in l:
                l.append(i)
        l.sort()
        if len(l) <= 1:
            return -1
        else:
            return int(l[-2])