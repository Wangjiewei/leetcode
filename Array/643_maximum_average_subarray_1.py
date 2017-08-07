
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if (len(nums)<k):
            return 0
        max_sum = 0
        for i in range(0,k):
            max_sum += nums[i]
        cur_sum = max_sum
        for j in range(1,len(nums) - k + 1):
            cur_sum = cur_sum - nums[j-1] + nums[j + k - 1]
            if(cur_sum > max_sum):
                max_sum = cur_sum
        return float(max_sum)/k

if __name__ =='__main__':

    a = [1,12,-5,-6,50,3]
    b = [0,1,1,3,3]
    c = [0,4,0,3,2]
    k = 4

    so = Solution()
    print so.findMaxAverage(b,k)