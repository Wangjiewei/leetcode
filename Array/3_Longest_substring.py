
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        maxLenStr = ""
        char_dic = {}

        i = -1
        j = -1

        while(j < len(s) - 1):
            # LSS right pointer move 1 position
            j += 1
            # if char in this position not in char_dic
            if (s[j] not in char_dic):
                # add this char into char_dic
                char_dic[s[j]] = j
                # current substring length: right pointer - left pointer
                strLen = j - i
                if(strLen > maxLen):
                    maxLen = strLen
                    maxLenStr = s[i+1:j+1]
            # if char in this position in char_dic
            else:
                # get this char's position in char_dic
                dup_pos = char_dic[s[j]]
                # remove all chars from left pointer to duplicate position
                for k in range(i+1, dup_pos):
                    char_dic.pop(s[k])
                # update left pointer
                i = dup_pos
                char_dic[s[j]] = j
        return maxLen


if __name__ =='__main__':
    a = "abcabcbb"
    b = "bbbbb"
    c = "pwwkew"
    d = "ruowzgiooobpple"
    so = Solution()
    print so.lengthOfLongestSubstring(a)
    print so.lengthOfLongestSubstring(b)
    print so.lengthOfLongestSubstring(c)
    print so.lengthOfLongestSubstring(d)