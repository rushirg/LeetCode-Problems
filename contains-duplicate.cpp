/*
 *Solution of problem 217
 *https://leetcode.com/problems/contains-duplicate/
 */
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        sort(nums.begin(), nums.end());
        for(int i=1; i<nums.size(); i++){
            if(nums[i] == nums[i-1])
                return true;
        }
        return false;
    }
};

/*
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
*/
