/*
 *Solution for problem 704
 *https://leetcode.com/problems/binary-search/
 */
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1, mid;
        while(low<=high){
            mid = (low+high)/2;
            if(nums[mid] == target)
                return mid;
            if(nums[mid] > target)
                high = mid - 1;
            if(nums[mid] < target)
                low = mid + 1;
        }
        return -1;
    }
};
