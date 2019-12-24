/*
 *Solution for problem 961
 *https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
 *
 */
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        int count = 0, tmp;
        int size = A.size();
        sort(A.begin(), A.end());
        for(int i=1; i<size; i++){
            if(A[i-1] == A[i]){
                count++;
            }
            else
                continue;
            if((count+1) == size/2){
                tmp = A[i];break;
            }

        }
        return tmp;
    }
};
