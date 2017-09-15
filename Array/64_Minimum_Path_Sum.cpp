//
//  64_Minimum_Path_Sum.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/9/15.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = (int)grid.size();
        int n = (int)grid[0].size();
        vector<vector<int>> res;
        res.resize(m);
        for(int i = 0; i < m; i++)
            res[i].resize(n);
        
        res[0][0] = grid[0][0];
        for(int i = 1; i<m; i++){
            res[i][0] = res[i-1][0] + grid[i][0];
        }
        for(int j = 1; j<n; j++){
            res[0][j] = res[0][j-1] + grid[0][j];
        }
        
        for(int i =1; i<m; i++) {
            for (int j = 1;j<n; j++){
                res[i][j] = min(res[i-1][j] , res[i][j-1]) + grid[i][j];
            }
        }
        
        return res[m-1][n-1];
    }
};




int main(){
    Solution solution;


    vector<vector<int>> vec;

    vector<int> v1 = {1,2,3};
    vector<int> v2 = {4,5,6};
    vector<int> v3 = {7,8,9};

    vec.push_back(v1);
    vec.push_back(v2);
    vec.push_back(v3);

    // 合并
    int v = solution.minPathSum(vec);
    // 输出
    cout<<v<<endl;
    return 0;
}
