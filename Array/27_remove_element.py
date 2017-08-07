class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if (len(nums) == 0):
            return 0
        j = 0
        for i in range(0, len(nums)):
            if (nums[i] != val):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return j



if __name__ =='__main__':

    a = [-4,-1,-1, 0, 1, 2]
    a2 = [1,1,2]
    so = Solution()
    print so.removeElement(a,2)
    print so.removeElement(a2,2)