/*
 *Solution of problem 383
 *https://leetcode.com/problems/ransom-note/
 */

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {

        int ransomArr[26]={0}, magazineArr[26]={0};
        for(int i=0; i<ransomNote.size(); i++){
            ransomArr[ransomNote[i] - 'a']++;
        }
        for(int i=0; i<magazine.size(); i++){
            magazineArr[magazine[i] - 'a']++;
        }
        for(int i=0; i<26; i++){
            if(magazineArr[i] < ransomArr[i])
                return false;
        }
        return true;
    }
};
