/*
 *Solution for problem 905
 *https://leetcode.com/problems/sort-array-by-parity/
 */
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> tmp;
        stack<int> s;
        for(int i=0; i<A.size(); i++){
            if(A[i] % 2 ==1){
                s.push(A[i]);
            }
            else{
                tmp.push_back(A[i]);
            }
        }
        while(!s.empty()){
            tmp.push_back(s.top());
            s.pop();
        }
        return tmp;
    }
};
