class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #
    #
    #     for i in range(0, len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if(nums[i] + nums[j] == target):
    #                 return (i,j)
    #     return (i,j)

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sum_map = {}

        for i in range(0, len(nums)):
            pair = target - nums[i]
            if(pair in sum_map):
                    return (sum_map[pair],i)
            sum_map[nums[i]] = i
        return (0,0)



if __name__ =='__main__':
    nums = [2, 7, 11, 15]
    target = 9
    so = Solution()
    print so.twoSum(nums, target)