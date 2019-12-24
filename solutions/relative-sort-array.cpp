/*
 *Solution for problem 1122
 *https://leetcode.com/problems/relative-sort-array/
 */
class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        int A[1001]={0};
        for(int i=0; i<arr1.size(); i++){
            A[arr1[i]]++;
        }
        vector<int> ans;
        for(int i=0; i<arr2.size(); i++){
            for(int j=0; j<A[arr2[i]]; j++)
                ans.push_back(arr2[i]);
            A[arr2[i]] = 0;
        }
        for(int i=0; i<1001; i++){
            if(A[i] != 0){
                for(int j=0; j<A[i]; j++)
                    ans.push_back(i);
            }
        }
        return ans;
    }
};
