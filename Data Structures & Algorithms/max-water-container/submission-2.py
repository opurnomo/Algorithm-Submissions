class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) -1

        while l < r:
            lh, rh, = heights[l], heights[r]
            area = max(area, min(lh, rh) * (r-l))
            if lh > rh:
                r -= 1
            else:
                l +=1
        return area
