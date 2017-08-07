class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        s = sorted(nums)
        res = set()
        for i in range(0,len(s)-3):
            for j in range(i+1, len(s)-2):
                start = j + 1
                end = len(s) - 1
                while(start < end):
                    if(s[i] + s[j] + s[start] + s[end] == target):
                        res.add((s[i], s[j], s[start],s[end]))
                        start += 1
                        end -= 1
                    elif(s[i] + s[j] + s[start] + s[end] < target):
                        start += 1
                    else:
                        end -= 1

        res_list = []
        for item in res:
            res_list.append([item[0], item[1], item[2], item[3]])
        return res_list

if __name__ =='__main__':

    a1 = [-1,0,1,2,-1,-4]
    b1 = -1
    a2 = [-3,-2,-1,0,0,1,2,3]
    b2 = 0
    so = Solution()
    print so.fourSum(a1,b1)
    print so.fourSum(a2,b2)
