/*
 *Solution of problem 167
 *https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 */

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int index1 = 0, index2 = numbers.size() - 1, sum;
        vector<int> ans;
        while(index1 < index2){
            sum = numbers[index1] + numbers[index2];
            if(sum > target){
                index2--;continue;
            }
            else if(sum < target){
                index1++; continue;
            }
            else{
                ans.push_back(index1 + 1);
                ans.push_back(index2 + 1);
                break;
            }
        }
        return ans;
    }
};
