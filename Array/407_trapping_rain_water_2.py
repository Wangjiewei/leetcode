import Queue

class Point(object):
    def __init__(self, priority, position):
        self.priority = priority
        self.position = position
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if(len(heightMap)==0):
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        res = 0
        mx = -1

        q = Queue.PriorityQueue()
        visited = [[0 for col in range(n)] for row in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if(i == 0 or i== m-1 or j==0 or j==n-1):
                    q.put(Point(heightMap[i][j],i*n + j))
                    visited[i][j] = 1

        dir = [[0,-1],[-1,0],[0,1],[1,0]]
        while (q.qsize()> 0):
            top = q.get()
            h = top.priority
            r = top.position / n
            c = top.position % n
            mx = max(mx, h)
            for i in range(0,len(dir)):
                x = r + dir[i][0]
                y = c + dir[i][1]
                if(x<0 or x>= m or y < 0 or y >= n or visited[x][y] == 1):
                    continue
                visited[x][y]=1
                if(heightMap[x][y] < mx):
                    res += mx - heightMap[x][y]
                q.put(Point(heightMap[x][y],x*n + y))

        return res



if __name__ =='__main__':
    a = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
    so = Solution()
    print so.trapRainWater(a)