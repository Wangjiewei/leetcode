class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        j = 0
        for i in range(0,len(nums)):
            if(nums[i]!=nums[j]):
                nums[i],nums[j+1] = nums[j+1], nums[i]
                j += 1

        return j+1

if __name__ =='__main__':

    a = [-4,-1,-1, 0, 1, 2]
    a2 = [1,1,2]
    so = Solution()
    print so.removeDuplicates(a)
    print so.removeDuplicates(a2)