//
//  409_Longest_Palindrome.cpp
//  LeetCode
//
//  Created by jiewei wang on 2017/9/7.
//  Copyright © 2017年 jiewei wang. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;


class Solution {
public:
    int longestPalindrome(string s) {
        int letters[52] = {0};
        int plength = 0;
        int hasCenter = 0;
        
        for (auto c: s)
            isupper(c) ? letters[c - 'A' + 26]++ : letters[c - 'a']++;
        
        for (int i = 0; i < 52; i++) {
            if (letters[i] % 2) {
                plength += letters[i] - 1;
                hasCenter = 1;
            } else {
                plength += letters[i];
            }
        }
        
        return plength + hasCenter;
    }
};


//int main()
//{
//    string a = "abccccdd";
//    int res;
//
//    Solution solu;
//    res = solu.longestPalindrome(a);
//
//    cout<<res<<endl;
//    
//    return 0;
//}
