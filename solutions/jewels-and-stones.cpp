/*
 *Solution for problem 771 
 *https://leetcode.com/problems/jewels-and-stones/
 */
#include<map>
class Solution {
public:
    int numJewelsInStones(string J, string S) {
        map<char, int> m;
        int count = 0;
        for(int i=0; i<S.length(); i++)
            m[S[i]]++;
        for(int i=0; i<J.length(); i++){
            count += m[J[i]];
        }
        return count;
    }
};
