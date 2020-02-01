/*
 * Solution of problem 33
 * 33. Search in Rotated Sorted Array
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 *
 * Credits: Nick White (https://youtu.be/QdVrY3stDD4)
 */

class Solution {
public:
    int search(vector<int>& nums, int target) {

        // handle empty vector case
        if(nums.size() == 0 || nums.empty())
            return -1;

        // initialize variables
        int size = nums.size(), left = 0, right = size-1, mid;

        // find index of the smallest element in the vector
        while(left < right){
            mid = left + (right - left) / 2;
            if(nums[mid] > nums[right])
                left = mid + 1;
            else
                right = mid;
        }

        // store the index of the smallest element
        int start = left;

        // re-initialize the variables
        left = 0, right = size - 1;
        mid = left + (right - left) / 2;


        // check which block holds the target value
        if(target >= nums[start] &&  target <= nums[right])
            left = start;
        else
            right = start;

        // perform binary search on selected block only
        while(left <= right){
            mid = left + (right - left) / 2;
            if(nums[mid] == target)
                return mid;
            if(nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;

    }
};
