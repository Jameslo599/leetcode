# Longest Consecutive Sequence

# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in dic:
                length = 1
                while n + length in dic:
                    length += 1
                ans = max(ans, length)
        return ans

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         dic = defaultdict(bool)
#         ans = 0
#         for n in nums:
#             if n not in dic:
#                 dic[n] = True
#         for i in range(len(nums)):
#             j = 1
#             if nums[i] - j in dic or nums[i] not in dic:
#                 continue
#             while nums[i] + j in dic:
#                 dic.pop(nums[i] + j)
#                 j+=1
#             dic.pop(nums[i])
#             ans = max(ans, j)
#         return ans