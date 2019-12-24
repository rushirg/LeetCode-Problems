/*
 *Solution for problem 268
 *https://leetcode.com/problems/missing-number/
 */
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0, size = nums.size();
        for(int n: nums){
            sum += n;
        }
        int totalSum = ((size+1) * (size))/2;
        return totalSum - sum;
    }
};
