/*
 *Solution for problem 977
 *https://leetcode.com/problems/squares-of-a-sorted-array/
 */

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        for(int i=0; i<A.size(); i++)
            A[i] = A[i] * A[i];
        sort(A.begin(), A.end());
        return A;
    }
};


/*Big-O(n) Solution using two pointers
 *
 *
 *class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        int N = A.size();
        int i, j=0;
        while( j<N && A[j] < 0)
            j += 1;
        i = j - 1;
        vector<int> ans;
        while( i>=0 && j<N ){
            if(A[i] * A[i] < A[j] * A[j]){
                ans.push_back(A[i]*A[i]);
                i -= 1;
            }
            else{
                ans.push_back(A[j] * A[j]);
                j += 1;
            }
        }
        while( i>=0 ){
            ans.push_back(A[i] *A[i]);
            i -= 1;
        }
        while( j<N ){
            ans.push_back(A[j] * A[j]);
            j += 1;
        }
        return ans;
    }
};
 *
 */
