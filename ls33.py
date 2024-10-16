# Max Water Container

# You are given an integer array heights where heights[i] represents the height of the ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4
# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = left = 0
        right = len(heights) - 1
        while left < right:
            ans = max(ans, (right - left)*min(heights[left], heights[right]))
            if heights[left] < heights[right]: left+=1
            else: right-=1
        return ans