class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        last_reach = 0
        reach = 0
        step = 0

        for i in range(0, len(nums)):
            if i > reach: break

            if i > last_reach:
                step += 1
                last_reach = reach
            reach = max(reach, i + nums[i])

        if reach < len(nums) -1:
            return 0

        return step


if __name__ =='__main__':

    a1 = [2,3,1,1,4]
    a3 = [0]

    so = Solution()
    print so.jump(a1)
    print so.jump(a3)