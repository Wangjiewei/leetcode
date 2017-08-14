class Solution(object):

    def biniary_serch(self, nums, start, end, target):
        if start == end and nums[start] == target:
            return start
        elif start == end and nums[start] != target:
            return -1

        mid = (start + end) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start] and target >= nums[start] and target <= nums[mid]:
            return self.biniary_serch(nums, start, mid - 1, target)
        elif nums[end] >= nums[mid] and target >= nums[mid] and target <= nums[end]:
            return self.biniary_serch(nums, mid + 1, end, target)
        elif nums[mid] >= nums[start] and (target < nums[start] or  target > nums[mid]):
            return self.biniary_serch(nums, mid + 1, end, target)
        elif nums[end] >= nums[mid] and (target > nums[end] or target < nums[mid]):
            return self.biniary_serch(nums, start, mid - 1, target)
        else:
            return -1


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        return self.biniary_serch(nums, 0, len(nums) - 1, target)




if __name__ =='__main__':

    a1 = [0,1,2,4,5,6,7]
    b1 = 6
    a2 = [4,5,6,7,0,1,2]
    b2 = 2
    a3 = [0,1,6,7,8,9]
    b3 = 4
    so = Solution()
    print so.search(a1,b1)
    print so.search(a2,b2)
    print so.search(a3,b3)