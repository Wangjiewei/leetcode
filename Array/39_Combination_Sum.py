class Solution(object):

    res_list = []
    stack = []


    def combine(self,candidates, target, start):
        if target < 0:
            return
        elif target == 0:
            self.res_list.append(self.stack[:])
        else:
            for i in range(start,len(candidates)):
                self.stack.append(candidates[i])
                self.combine(candidates, target - candidates[i], i)
                self.stack.pop(len(self.stack)-1)


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res_list = []
        self.stack = []

        candidates = sorted(candidates)

        self.combine(candidates, target, 0)

        return self.res_list





if __name__ =='__main__':

    a1 = [2, 3, 6, 7]
    b1 = 7
    so = Solution()
    print so.combinationSum(a1, b1)

