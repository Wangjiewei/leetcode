class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 0:
            return 0

        local = nums[0]
        gsum = nums[0]

        for i in range(1, len(nums)):
            local = max(nums[i], local + nums[i])
            gsum = max(gsum, local)

        return gsum

if __name__ =='__main__':

    a1 = [-2,1,-3,4,-1,2,1,-5,4]


    so = Solution()
    print so.maxSubArray(a1)