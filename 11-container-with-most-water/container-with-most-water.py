class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = float('-inf')
        while l<r:
            area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, area)

            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return max_area
