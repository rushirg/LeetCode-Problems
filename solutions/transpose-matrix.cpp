/*
 *Solution for problem 867
 *https://leetcode.com/problems/transpose-matrix/
 */

// Runtime: 28ms 
class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
     
        vector<vector<int>> ans;
        int out = A.size(), in = A[0].size();
        for(int i=0; i<in; i++){
            vector<int> tmp;
            for(int j=0; j<out; j++)
                tmp.push_back(A[j][i]);
            ans.push_back(tmp);
        }
        return ans;
    }
};


/*Python Solution
 *Runtime: 60ms
 *
 *class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)
 *
 * /

