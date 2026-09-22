class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        for i in range(min(l1, l2), 0, -1):
            if l1 % i == 0 and l2 % i == 0:
                t1 = l1 // i
                t2 = l2 // i

                if str1[:i] * t1 == str1 and str1[:i] * t2 == str2:
                    return str1[:i]

        return ""