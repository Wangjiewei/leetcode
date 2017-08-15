class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if len(nums) == 0:
            return False

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[start]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1

        return False



if __name__ =='__main__':

    a1 = [1,3,1,1,1]
    b1 = 3
    a2 = [4,5,6,7,0,1,2]
    b2 = 2
    a3 = [0,1,6,7,8,9]
    b3 = 4
    so = Solution()
    print so.search(a1,b1)
    print so.search(a2,b2)
    print so.search(a3,b3)