/*
 *Solution for problem 1200
 *https://leetcode.com/problems/minimum-absolute-difference/
 */
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {

        vector<vector<int>> ans;
        int minDiff = INT_MAX;
        sort(arr.begin(), arr.end());
        for(int i=0,j=i+1; j<arr.size(); i++, j++){
            vector<int> tmp;
            if(abs(arr[j] - arr[i]) <= minDiff){
                minDiff = abs(arr[j] - arr[i]);
            }
        }
        for(int i=0,j=i+1; j<arr.size(); i++, j++){
            vector<int> tmp;
            if(abs(arr[j] - arr[i]) <= minDiff){
                tmp.push_back(arr[i]);
                tmp.push_back(arr[j]);
                ans.push_back(tmp);
            }
        }
        return ans;
    }
};
