/*
 *Solution for problem 520
 *https://leetcode.com/problems/detect-capital/
 */
class Solution {
public:
    bool detectCapitalUse(string word) {
        int prev;
        if(word[0] >= 'A' && word[0] <= 'Z')
            prev = 0;
        else
            prev = 1;
        for(int i=1; i<word.size(); i++){
            if(word[i] >= 'A' && word[i] <='Z'){
                if(prev == 0){
                    continue;
                }
                else
                    return false;
            }
            if(word[i] >= 'a' && word[i] <= 'z'){
                if(prev == 0 and i == 1)
                    prev = 1;
                if(prev == 1)
                    continue;
                else
                    return false;
            }
        }
        return true;
    }
};
