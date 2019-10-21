/*
 *Solution for problem 852
 *https://leetcode.com/problems/peak-index-in-a-mountain-array/
 */
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {

        int i, j;
        for(i = 0, j = i + 1; j < A.size(); i+=1, j+=1 ){
            if(A[i] > A[j])
                break;
        }
        return i;
    }
};
