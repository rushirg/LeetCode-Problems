/*
 *Solution of problem 171
 *https://leetcode.com/problems/excel-sheet-column-number/
 */
class Solution {
public:
    int titleToNumber(string s) {
        int size = s.size(), ans = 0;
        for(int i=0, j=size - 1; i<size; i++, j--){
            ans = ans + (s[i] - 'A' + 1) * pow(26, j);
        }
        return ans;
    }
};
