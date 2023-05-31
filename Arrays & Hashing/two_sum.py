class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}
        for i, num in enumerate(nums):
            if (target - num) in index_map:
                return i, index_map[target - num]
            index_map[num] = i


soln = Solution()
ans = soln.twoSum([3, 2, 4], 6)
print(ans)
