//
//  215_Kth_Largest_Element_in_an_Array.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/9/14.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left = 0, right = nums.size() - 1;
        while (true) {
            int pos = partition(nums, left, right);
            if (pos == k - 1) return nums[pos];
            else if (pos > k - 1) right = pos - 1;
            else left = pos + 1;
        }
    }
    int partition(vector<int>& nums, int left, int right) {
        int pivot = nums[left], l = left + 1, r = right;
        while (l <= r) {
            if (nums[l] < pivot && nums[r] > pivot) {
                swap(nums[l++], nums[r--]);
            }
            if (nums[l] >= pivot) ++l;
            if (nums[r] <= pivot) --r;
        }
        swap(nums[left], nums[r]);
        return r;
    }
};



//int main(){
//    
//    Solution solution;
//    
//    vector<int> nums;
//    nums.push_back(3);
//    nums.push_back(2);
//    nums.push_back(1);
//    nums.push_back(5);
//    nums.push_back(6);
//    nums.push_back(4);
//
//
//    int k=1;
//    int ans = solution.findKthLargest(nums, k);
//    cout<<ans<<endl;
//
//}
