
class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        start = i + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



if __name__ =='__main__':

    a1 = [1,2,3]
    a2 = [3,2,1]
    a3 = [1,1,5]
    a4 = [1]
    a5 = [1,3,2]
    so = Solution()
    print so.nextPermutation(a1)
    print so.nextPermutation(a2)
    print so.nextPermutation(a3)
    print so.nextPermutation(a4)
    print so.nextPermutation(a5)