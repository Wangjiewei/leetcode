class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        res = 0
        pair_sum = {}
        if(len(A) == 0 or len(B) == 0 or len(C) == 0 or len(D) == 0 ):
            return 0
        for i in range(0,len(A)):
            for j in range(0,len(B)):
                if( (A[i] + B[j]) not in pair_sum ):
                    pair_sum[A[i] + B[j]] = 0
                pair_sum[A[i] + B[j]] += 1
        for i in range(0, len(C)):
            for j in range(0,len(D)):
                if( (0 - C[i] - D[j]) in pair_sum):
                    res += pair_sum[0 - C[i] - D[j]]
        return res


if __name__ =='__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    so = Solution()
    print so.fourSumCount(A,B,C,D)

