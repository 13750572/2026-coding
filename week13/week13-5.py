# LeetCode 2542. Maximum Subsequence Score
# 挑 k 個 index, 讓 nums1 對應的 k 個數相加, 再乘 min(nums2對應k個數) 希望最大
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 先把 nums2 跟 nums1 合併起來 (以 nums2 作為排序依據)
        N = len(nums1) # 陣列的長度
        a = [ (nums2[i], nums1[i]) for i in range(N)] # 左右合併起來

        # 依據 nums2 的大小，由大到小排序
        a.sort(reverse=True)

        # heap 裡面要放的是 nums1 的數值，也就是 a[i][1]
        heap = [a[i][1] for i in range(k)] # 找到最前面的 k 組數字, 加入 heap 資料結構
        heapify(heap) # 變成最小堆疊，之後可以隨時吐出裡面最小的 nums1
        total = sum(heap)

        # 因為已經由大到小排，前 k 項中最小的 nums2 就是 a[k-1][0]
        ans = total * a[k-1][0] # 前 k 項的 nums1 加總 及對應最小的 nums2 相乘

        # 繼續嘗試後面的組合
        for i in range(k, len(nums2)):
            n2, n1 = a[i] # n2 是當前最小的 nums2, n1 是準備加入的 nums1
            heappush(heap, n1) # 將新的 nums1 放入 heap
            total += n1 - heappop(heap) # 加總加上新數字，並吐出目前 heap 裡最小的數字
            ans = max(ans, total * n2) # 更新最大得分

        return ans
