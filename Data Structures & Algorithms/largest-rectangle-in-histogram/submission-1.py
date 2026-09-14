class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stk = [-1]
        heights = heights + [0]

        for i in range(len(heights)):

            while stk[-1] != -1 and heights[i] < heights[stk[-1]]:
                height = heights[stk.pop()]
                width = i - (stk[-1] + 1)

                area = height * width
                max_area = max(max_area, area)

            stk.append(i)
        
        return max_area