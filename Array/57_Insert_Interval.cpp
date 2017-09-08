//
//  57_Insert_Interval.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/9/8.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};


class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval> res = intervals;
        int i = 0, overlap = 0, n = (int)res.size();
        while (i < n) {
            if (newInterval.end < res[i].start) break;
            else if (newInterval.start > res[i].end) {}
            else {
                newInterval.start = min(newInterval.start, res[i].start);
                newInterval.end = max(newInterval.end, res[i].end);
                ++overlap;
            }
            
            ++i;
        }
        
        if (overlap > 0) res.erase(res.begin() + i - overlap, res.begin() + i);
        res.insert(res.begin() + i - overlap, newInterval);

        
        return res;
    }
};



//int main(){
//    Solution solution;
//    Interval in1(1,2);
//    Interval in2(3,5);
//    Interval in3(6,7);
//    Interval in4(8,10);
//    Interval in5(12,16);
//    
//    Interval ins(4,9);
//
//    vector<Interval> vec;
//    vec.push_back(in1);
//    vec.push_back(in2);
//    vec.push_back(in3);
//    vec.push_back(in4);
//    vec.push_back(in5);
//    // 合并
//    vector<Interval> v = solution.insert(vec,ins);
//    // 输出
//    for(int i = 0;i < v.size();i++){
//        Interval in = v[i];
//        cout<<"["<<in.start<<","<<in.end<<"]"<<endl;
//    }//for
//    return 0;
//}
