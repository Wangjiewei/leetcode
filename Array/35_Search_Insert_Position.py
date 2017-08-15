class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if nums[start] < target:
            return start + 1
        else:
            return start


if __name__ =='__main__':

    a1 = [1,3,5,6]
    b1 = 0

    so = Solution()
    print so.searchInsert(a1,b1)
