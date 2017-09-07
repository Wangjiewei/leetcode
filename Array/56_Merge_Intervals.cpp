//
//  56_Merge_Intervals.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/9/7.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;


/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */

struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};


class Solution {
public:
    static bool comp(const Interval &a, const Interval &b) {
        return (a.start < b.start);
    }
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;
        if (intervals.empty()) return res;
        sort(intervals.begin(), intervals.end(), comp);
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i) {
            if (res.back().end >= intervals[i].start){
                res.back().end = max(res.back().end, intervals[i].end);
            }else{
                res.push_back(intervals[i]);
            }
        }
        return res;
    }
};


//int main(){
//    Solution solution;
//    Interval in1(1,3);
//    Interval in2(2,6);
//    Interval in3(8,10);
//    Interval in4(15,18);
//    
//    vector<Interval> vec;
//    vec.push_back(in1);
//    vec.push_back(in2);
//    vec.push_back(in3);
//    vec.push_back(in4);
//    // 合并
//    vector<Interval> v = solution.merge(vec);
//    // 输出
//    for(int i = 0;i < v.size();i++){
//        Interval in = v[i];
//        cout<<"["<<in.start<<","<<in.end<<"]"<<endl;
//    }//for
//    return 0;
//}
