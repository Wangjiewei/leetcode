class Solution(object):

    def findplace(self, nums1, target, m):
        pos = 0

        while target >= nums1[pos] and pos < m:
            pos += 1

        return pos

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        for j in range(0, n):
            # find the right place in nums1
            pos = self.findplace(nums1, nums2[j], m + j)
            for i in range(m + j, pos, -1):
                nums1[i] = nums1[i -1]
            nums1[pos] = nums2[j]






if __name__ =='__main__':

    a1 = [2, 3, 6, 7, 0,0,0,0,0]
    a2 = [1, 2, 6, 7, 10]
    so = Solution()

    print so.merge(a1, 4, a2, len(a2))