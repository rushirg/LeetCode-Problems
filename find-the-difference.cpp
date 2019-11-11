/*
 *Solution of problem 389
 *https://leetcode.com/problems/find-the-difference/
 */
class Solution {
public:
    char findTheDifference(string s, string t) {
        int arr[26] = {0};
        for(char ch: s)
            arr[ch - 'a']++;
        for(char ch: t){
            if(arr[ch - 'a'] == 0)
                return ch;
            arr[ch - 'a']--;
        }
        return NULL;
    }
};

/*
 * class Solution {
public:
    char findTheDifference(string s, string t) {
        char ans = 0;
        for(char c: s) ans ^= c;
        for(char c: t) ans ^= c;
        return ans;
    }
};
*
* /
