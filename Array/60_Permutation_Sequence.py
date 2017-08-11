import math
class Solution(object):

    res_list = ""
    active = []

    def permutation(self,n,k):
        if(n == 1):
            self.res_list += str(self.active[0])
            return

        highest_idx = (k - 1) / math.factorial(n-1) + 1
        tmp_list = sorted(self.active)
        highest = tmp_list[highest_idx - 1]
        self.res_list += str(highest)
        self.active.remove(highest)
        rest = (k + 1)  % math.factorial(n -1) - 1
        self.permutation(n - 1, rest)


    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res_list = ""
        self.active = [i +1 for i in range(n)]

        self.permutation(n,k)

        return self.res_list

if __name__ =='__main__':


    so = Solution()
    print so.getPermutation(3,5)
    print so.getPermutation(4,9)
    print so.getPermutation(9,3)
    print so.getPermutation(8,100)
    print so.getPermutation(7,1)