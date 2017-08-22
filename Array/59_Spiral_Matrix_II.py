class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n == 0:
            return []

        res_list =[[0 for col in range(n)] for row in range(n)]

        direc = [[0, 1],
                 [1, 0],
                 [0, -1],
                 [-1, 0]]

        stand = [0,0]
        next_dir = 0
        cnt = 1
        res_list[0][0] = cnt

        while cnt < n * n:

            next_i = stand[0] + direc[next_dir][0]
            next_j = stand[1] + direc[next_dir][1]
            if next_i >= n or next_j >= n:
                next_dir = (next_dir + 1) % 4
                next_i = stand[0] + direc[next_dir][0]
                next_j = stand[1] + direc[next_dir][1]
            if res_list[next_i][next_j] == 0:
                cnt += 1
                res_list[next_i][next_j] = cnt
                stand[0] = next_i
                stand[1] = next_j
            else:
                next_dir = (next_dir + 1) % 4

        return res_list


if __name__ =='__main__':
    n1 = 5
    so = Solution()
    print so.generateMatrix(n1)