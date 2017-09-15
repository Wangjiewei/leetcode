//
//  63_Unique_Paths_II.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/9/8.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = (int)obstacleGrid.size();
        int n = (int)obstacleGrid[0].size();
        vector<vector<int>> res;
        res.resize(m);
        for(int i = 0; i < m; i++)
            res[i].resize(n);
        
        //遇到障碍就退出，后面的都走不到，保持默认值0即可
        for(int i = 0; i<m && obstacleGrid[i][0] == 0; i++){
            res[i][0] = 1;
        }
        for(int j = 0; j<n && obstacleGrid[0][j] == 0; j++){
            res[0][j] = 1;
        }
        
        for(int i =1; i<m; i++) {
            for (int j = 1;j<n; j++){
                if(obstacleGrid[i][j] == 1){
                    res[i][j] = 0;
                }else{
                    res[i][j] = res[i-1][j] + res[i][j-1];
                }
            }
        }
        
        return res[m-1][n-1];
    }
};

//int main(){
//    Solution solution;
//
//
//    vector<vector<int>> vec;
//    
//    vector<int> v1 = {0,0,0};
//    vector<int> v2 = {0,1,0};
//    vector<int> v3 = {0,0,0};
//    
//    vec.push_back(v1);
//    vec.push_back(v2);
//    vec.push_back(v3);
// 
//    // 合并
//    int v = solution.uniquePathsWithObstacles(vec);
//    // 输出
//    cout<<v<<endl;
//    return 0;
//}
