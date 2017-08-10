class Solution(object):

    res_list = []
    visited = []
    stack = []

    def permute(self,nums):
        if len(self.stack) == len(nums):
            self.res_list.append(self.stack[:])
            return


        for i in range(0, len(nums)):
            if i > 0 and self.visited[i - 1] != 0 and nums[i] == nums[i - 1]:
                continue

            if self.visited[i] == 0:
                self.visited[i] = 1
                self.stack.append(nums[i])
                self.permute(nums)
                self.stack.pop(len(self.stack)-1)
                self.visited[i] = 0


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.res_list = []
        self.visited = [0 for i in range(len(nums))]

        if len(nums) == 0:
            return self.res_list

        nums = sorted(nums)
        self.stack = []

        self.permute(nums)

        return self.res_list





if __name__ =='__main__':

    a1 = [1,2,3]
    a2 = [1,1,2]
    a3 = [1]
    a4 = []
    a5 = [2,2,1,1]
    so = Solution()
    print so.permuteUnique(a1)
    print so.permuteUnique(a2)
    print so.permuteUnique(a3)
    print so.permuteUnique(a4)
    print so.permuteUnique(a5)