/*
 *Solution for problem 942
 *https://leetcode.com/problems/di-string-match/
 */

class Solution {
public:
    vector<int> diStringMatch(string S) {
        int inc = 0, dec = S.length();
        vector<int> ans;
        for(int i=0; i<S.length(); i++){
            if(S[i] == 'I'){
                ans.push_back(inc);
                inc+=1;
            }
            else{
                ans.push_back(dec);
                dec-=1;
            }
        }
        if(ans.size() == S.length())
            ans.push_back(inc);
        return ans;
    }
};
