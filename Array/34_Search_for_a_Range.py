class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1,-1]

        start = 0
        end = len(nums) - 1

        pos = -1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                pos = mid
                break
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        if pos == -1:
            return [-1,-1]
        else:
            left = pos
            right = pos
            while left > 0 and nums[left - 1] == nums[left]:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] == nums[right]:
                right += 1
            return [left, right]


if __name__ =='__main__':

    a1 = [5, 7, 7, 8, 8, 10]
    b1 = 8
    a2 = [2,2]
    b2 = 2
    so = Solution()
    #print so.searchRange(a1,b1)
    print so.searchRange(a2,b2)