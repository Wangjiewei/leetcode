class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if len(matrix) == 0:
            return []

        res = []
        m = len(matrix)
        n = len(matrix[0])
        visited = [0 for i in range(m * n)]
        direc = [[0,1],
                 [1,0],
                 [0,-1],
                 [-1,0]]

        stand = [0,0]
        res.append(matrix[0][0])
        visited[0] = 1
        next_dir = 0
        cnt = 1
        while cnt < m * n:

            next_i = stand[0] + direc[next_dir][0]
            next_j = stand[1] + direc[next_dir][1]
            if next_i >= m or next_j >= n:
                next_dir = (next_dir + 1) % 4
                next_i = stand[0] + direc[next_dir][0]
                next_j = stand[1] + direc[next_dir][1]
            if visited[next_i * n + next_j] == 0:
                res.append(matrix[next_i][next_j])
                visited[next_i * n + next_j] = 1
                stand[0] = next_i
                stand[1] = next_j
                cnt += 1
            else:
                next_dir = (next_dir + 1) % 4

        return res



if __name__ =='__main__':

    a1 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

    a2 = []
    a3 = [[1]]
    a4 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
    a5 = [[3],[2]]
    so = Solution()
    print so.spiralOrder(a1)
    print so.spiralOrder(a2)
    print so.spiralOrder(a3)
    print so.spiralOrder(a4)
    print so.spiralOrder(a5)