/*
 *Solution of problem 448
 *https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 */


//efficient approach: O(n) runtime with O(1) space 
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {

        vector<int> ans;
        for(int i=0; i<nums.size(); i++){
            int m = abs(nums[i]) - 1;
            nums[m] = nums[m]>0 ? -nums[m] : nums[m];
        }
        for(int i=0; i<nums.size(); i++){
            if(nums[i] > 0)
                ans.push_back(i+1);
        }
        return ans;
    }
};


/*Trivial approach
 *
 *class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        vector<int> ans;
        sort(nums.begin(), nums.end());
        int numsSize = nums.size();
        for(int i=1; i<=numsSize; i++){
            if(not binary_search(nums.begin(), nums.end(), i)){
                ans.push_back(i);
            }
        }
        return ans;
    }
};
*
*/
