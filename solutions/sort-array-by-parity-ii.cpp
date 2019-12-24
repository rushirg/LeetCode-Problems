/*
 *Solution for problem 922
 *https://leetcode.com/problems/sort-array-by-parity-ii/
 */
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> ans(A.size());
        int e = 0, o = 1;
        for(int i=0; i<A.size(); i++){
            if(A[i] % 2 == 0){
                ans[e] = A[i];
                e += 2;
            }
            else{
                ans[o] = A[i];
                o += 2;
            }
        }
        return ans;
    }
};

/*In-place re-arrage
 *
 * class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        int j = 1, i, tmp;
        for(i=0; i<A.size(); i+=2){
            if(A[i] % 2){
                while(A[j] % 2)
                    j += 2;
                tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
        return A;
    }
};
 */
