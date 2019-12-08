/*
 *Solution of problem 283
 *https://leetcode.com/problems/move-zeroes/
 */

class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        int i = 0, j = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] != 0){
                if(nums[j] == 0){
                    nums[j++] = nums[i];
                    nums[i] = 0;
                }
                else{
                    j++;
                }
            }
        }
    }
};


/*
 *Using extra space
 * 
 * class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        vector<int> result;
        for(int x: nums){
            if(x != 0)
                result.push_back(x);
        }
        for(int i=result.size(); i<nums.size(); i++){
            result.push_back(0);
        }
        nums = result;
    }
};
*
*
*/
