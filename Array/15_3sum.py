class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        res = set()
        for k in range(0,len(s)):
            if(s[k]>0): break
            target = 0 - s[k]
            i = k + 1
            j = len(s) -1
            while(i < j):
                if(s[i] + s[j] == target):
                    res.add((s[k],s[i],s[j]))
                    while(i<j and s[i] == s[i+1]): i+=1
                    while(i<j and s[j] == s[j-1]): j-=1
                    i+=1
                    j-=1
                elif(s[i]+s[j]<target): i+=1
                else: j-=1
        res_list = []
        for item in res:
            res_list.append([item[0],item[1],item[2]])
        return res_list


if __name__ =='__main__':

    a = [-1, 0, 1, 2, -1, -4]
    so = Solution()
    print so.threeSum(a)