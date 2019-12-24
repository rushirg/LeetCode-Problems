/*
 *Solution of problem 169
 *https://leetcode.com/problems/majority-element/
 */
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int max=nums[0], count = 1;
        for(int i=1; i<nums.size(); i++){

            if(nums[i] == max){
                count += 1;
            }
            else{
                count -= 1;
                if(count <= 0){
                    max = nums[i];
                    count = 1;
                }
            }
        }
        return max;
    }
};
