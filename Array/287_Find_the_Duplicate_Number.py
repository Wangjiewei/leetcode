class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min = 0
        max = len(nums) - 1

        while min <= max:
            mid = (min + max) / 2

            cnt = 0
            for i in range(0, len(nums)):
                if nums[i] <= mid:
                    cnt += 1

            if cnt > mid:
                max = mid -1
            else:
                min = mid + 1

        return min




if __name__ =='__main__':

    a1 = [3,4,1,1]

    so = Solution()
    print so.findDuplicate(a1)