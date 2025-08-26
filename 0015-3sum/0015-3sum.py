class Solution(object):
    def threeSum(self, nums):
       
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left_val = nums[left]
                    while left < right and nums[left] == left_val:
                        left += 1

                    right_val = nums[right]
                    while left < right and nums[right] == right_val:
                        right -= 1

        return res
