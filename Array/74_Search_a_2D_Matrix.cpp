//
//  74_Search_a_2D_Matrix.cpp
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
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = (int)matrix.size();
        int n = (int)matrix[0].size();
        
        int low = 0;
        int hig = m - 1;
        
        while (low <= hig){
            int mid = (low + hig) / 2;
            if(matrix[mid][0] == target) return true;
            else if(matrix[mid][0] > target) hig = mid - 1;
            else if(matrix[mid][0] < target) low = mid + 1;
        }
        
        int row = hig;
        if (row < 0) return false;
        
        low = 0;
        hig = n - 1;
        
        while(low <=  hig){
            int mid = (low + hig) / 2;
            if (matrix[row][mid] == target) return true;
            else if (matrix[row][mid] > target) hig = mid - 1;
            else if (matrix[row][mid] < target) low = mid + 1;
        }
        
        return false;
    }
};


int main(){
    Solution solution;


    vector<vector<int>> vec;

    vector<int> v1 = {1,   3,  5,  7};
    vector<int> v2 = {10, 11, 16, 20};
    vector<int> v3 = {23, 30, 34, 50};

    vec.push_back(v1);
    vec.push_back(v2);
    vec.push_back(v3);

    //
    bool v = solution.searchMatrix(vec,15);
    // 输出
    cout<<v<<endl;
    return 0;
}
