//
//  174_Dungeon_Game.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/9/29.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        
        int m = (int)dungeon.size();
        int n = (int)dungeon[0].size();

        vector<vector<int>> res;
        
        res.resize(m);
        for(int i = 0; i < m; i++)
            res[i].resize(n);
        
        
        res[m - 1][n - 1] = dungeon[m - 1][n - 1] > 0 ? 0 : -dungeon[m - 1][n - 1];
        for(int i = m - 2; i>=0 ; i--)
            res[i][n-1] = dungeon[i][n - 1] >= res[i + 1][n - 1] ? 0 : res[i + 1][n - 1] - dungeon[i][n - 1];
        for(int j = n - 2; j>=0; j--)
            res[m - 1][j] = dungeon[m - 1][j] >= res[m - 1][j + 1] ? 0 : res[m - 1][j + 1] - dungeon[m - 1][j];
        

        
        for(int i =m -2; i>=0; i--) {
            for (int j = n-2;j>=0; j--){
                int down = dungeon[i][j] >= res[i + 1][j] ? 0 : res[i + 1][j] - dungeon[i][j];
                int right = dungeon[i][j] >= res[i][j + 1] ? 0 : res[i][j + 1] - dungeon[i][j];
                res[i][j] = min(down, right);
            }
        }
        
        return res[0][0] + 1;
    }
};


int main(){
    Solution solution;


    vector<vector<int>> vec;

//    vector<int> v1 = {-2,-3,3};
//    vector<int> v2 = {-5,-10,1};
//    vector<int> v3 = {10,30,-5};
    
    vector<int> v1 = {0,0,0};
    vector<int> v2 = {1,1,-1};


    vec.push_back(v1);
    vec.push_back(v2);
//    vec.push_back(v3);

    // 合并
    int v = solution.calculateMinimumHP(vec);
    // 输出
    cout<<v<<endl;
    return 0;
}
