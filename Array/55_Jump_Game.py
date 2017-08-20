class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        last_pos = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0


if __name__ =='__main__':

    a1 = [2,3,1,1,4]
    a2 = [3,2,1,0,4]
    a3 = [0]

    so = Solution()
    print so.canJump(a1)
    print so.canJump(a2)
    print so.canJump(a3)