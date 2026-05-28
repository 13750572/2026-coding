from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(i):
            if i >= len(nums): return 0 # 沒房子可搶了，錢是 0

            # 兩種選擇：(搶這間，跳過下一間) or (不搶這間，直接看下一間)
            return max(nums[i] + helper(i + 2), helper(i + 1))

        return helper(0) # 從第 0 間房子開始選
