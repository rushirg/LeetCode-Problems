/*
 *Solution of problem 260
 *https://leetcode.com/problems/single-number-iii/
 */

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xorOp = 0;
        for(int n: nums)
            xorOp ^= n;
        int mask = 1, a = 0, b = 0;
        while((xorOp&mask) == 0)
            mask <<= 1;
        for(int n: nums){
            if(n&mask)
                a ^= n;
            else
                b ^= n;
        }
        vector<int> result;
        result.push_back(a);
        result.push_back(b);
        return result;
    }
};


/*
 *
 * class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {

        vector<int> result;
        int size = nums.size();
        sort(nums.begin(), nums.end());
        for(int i=0; i < size - 1;){
            if(nums[i] == nums[i+1]){
                i+=2;continue;
            }
            else{
                result.push_back(nums[i]);
                i = i + 1;
            }
        }
        if(nums[size - 2] != nums[size - 1])
            result.push_back(nums[size-1]);
        return result;
    }
};
*
*/
