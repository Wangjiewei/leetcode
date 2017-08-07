import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sorted(nums)
        closest = sys.maxint

        for k in range(0, len(s)):
            i = k + 1
            j = len(s) - 1
            while (i < j):
                if (s[i] + s[j] + s[k] == target):

                    while (i < j and s[i] == s[i + 1]): i += 1
                    while (i < j and s[j] == s[j - 1]): j -= 1
                    i += 1
                    j -= 1
                    return target
                elif (s[i] + s[j] + s[k] < target):
                    if (abs(s[i] + s[j] + s[k] - target) < abs(target - closest)):
                        closest = s[i] + s[j] + s[k]
                    i += 1
                else:
                    if (abs(s[i] + s[j] + s[k] - target) < abs(target - closest)):
                        closest = s[i] + s[j] + s[k]
                    j -= 1

        return closest

if __name__ =='__main__':

    a = [-1, 2, 1, -4]
    b = [0,1,2]
    k1 = 1
    k2 = 3
    so = Solution()
    print so.threeSumClosest(a,k1)
    print so.threeSumClosest(b, k2)