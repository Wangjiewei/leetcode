# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):

    def isBadVersion(self,version):

        v = [True, False]
        return v[version]

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0

        start = 1
        end = n
        while start < end:

            mid = (start + end) / 2
            if self.isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start




if __name__ =='__main__':

    so = Solution()
    print so.firstBadVersion(2)