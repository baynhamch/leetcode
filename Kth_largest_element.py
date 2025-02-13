class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l , p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)

nums = [3,2,1,5,6,4]
k = 2
# Output: 5

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
# Output: 4

s = Solution()
print(s.findKthLargest(nums, k))
print(s.findKthLargest(nums2, k2))
