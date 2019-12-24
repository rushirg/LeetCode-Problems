/*
 *Solution for problem 1051
 *https://leetcode.com/problems/height-checker/
 */
class Solution {
public:
    int heightChecker(vector<int>& heights) {

        vector<int> tmp = heights;
        int count = 0;
        sort(tmp.begin(), tmp.end());
        for(int i=0; i<tmp.size(); i++){
            if(tmp[i] != heights[i])
                count++;
        }
        return count;
    }
};
