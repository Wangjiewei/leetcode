class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_i = 0
        max_j = len(height) - 1

        left = 0
        right = len(height) - 1

        ans = 0

        if(len(height) == 0):
            return ans

        while(left < right):
            if(height[left]< height[right]):
                if(height[left] > height[max_i]):
                    max_i = left
                else:
                    ans += height[max_i] - height[left]
                left += 1
            else:
                if(height[right] > height[max_j]):
                    max_j = right
                else:
                    ans += height[max_j] - height[right]
                right -= 1
        return ans




if __name__ =='__main__':
    a = [0,1,0,2,1,0,1,3,2,1,2,1]
    so = Solution()
    print so.trap(a)