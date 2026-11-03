class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m_c = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= m_c:
                candies[i] = True
            else:
                candies[i] = False
        return candies
