//
//  73_Set_Matrix_Zeroes.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/10/9.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
        int rowFlag = 0;
        int colFlag = 0;
        
        int i,j;
        
        int m = (int)matrix.size();
        int n = (int)matrix[0].size();
        
        for (i = 0; i<m; i++)
            if (matrix[i][0] == 0)
                colFlag = 1;
        for (j = 0; j<n; j++)
            if (matrix[0][j] == 0)
                rowFlag = 1;
        
        for (i = 1;i<m; i++){
            for (j = 1;j<n;j++){
                if (matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        for (i = 1;i<m;i++)
            for (j = 1;j<n;j++)
                if(matrix[i][0] == 0 or matrix[0][j] == 0)
                    matrix[i][j] = 0;
        
        if (rowFlag == 1)
            for (j = 0; j<n; j++)
                matrix[0][j] = 0;
        if (colFlag == 1)
            for (i = 0; i<m; i++)
                matrix[i][0] = 0;
        
    }
};



int main(){
    Solution solution;


    vector<vector<int>> vec;

    vector<int> v1 = {-2,-3,3};
    vector<int> v2 = {-5,0,1};
    vector<int> v3 = {10,30,-5};

    vec.push_back(v1);
    vec.push_back(v2);
    vec.push_back(v3);

    //
    solution.setZeroes(vec);
    // 输出
//    cout<<vec<<endl;
    return 0;
}


