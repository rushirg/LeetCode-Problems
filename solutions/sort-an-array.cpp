/*
 *Solution of problem 912
 *https://leetcode.com/problems/sort-an-array/
 */

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums;
    }
};


// We can implement a quick-sort here to be much efficient as the STL sort uses an introsort which is a hybrid sorting approach
