/*
 *Solution of problem 217
 *https://leetcode.com/problems/contains-duplicate/
 */

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> arr;
        for(int n: nums){
            arr[n] = arr[n] + 1;
            if(arr[n] > 1)
                return true;
        }
        return false;
    }
};
