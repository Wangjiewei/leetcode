
class Solution(object):
    def findKth(self, nums1, nums2, k):

        p = 0
        q = 0
        for i in range(0, k):
            if (p>=len(nums1) and q<len(nums2)):
                q+=1
            elif (q>=len(nums2) and p<len(nums1)):
                p+=1
            elif(nums1[p]> nums2[q]):
                q+=1
            else:
                p+=1

        if(p>=len(nums1)):
            return nums2[q]
        elif(q>=len(nums2)):
            return nums1[p]
        else:
            if(nums1[p] < nums2[q]):
                return nums1[p]
            else:
                return nums2[q]


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1 = len(nums1)
        len2 = len(nums2)

        total = len1 + len2

        if( total % 2 == 0):
            return (self.findKth(nums1, nums2, total / 2 - 1 ) + self.findKth(nums1, nums2, total / 2 )) / 2.0;
        else:
            return self.findKth(nums1, nums2, total / 2 );




if __name__ =='__main__':

    nums1 = [1, 3]
    nums2 = [2]

    so = Solution()

    print so.findMedianSortedArrays(nums1, nums2)