class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)

        return[(curNum + extraCandies >= maxCandies) for curNum in candies]