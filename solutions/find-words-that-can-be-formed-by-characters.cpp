/*
 *Solution for problem 1160
 *https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
 *
 */

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {


        int wordsLen = words.size(), charsLen = chars.length();
        int ch[26]={0};

        for(int i=0; i<charsLen; i++){
            ch[chars[i]-'a']++;
        }

        int ans=0;
        int i,j;
        for(i=0; i<wordsLen; i++){
            int tmpCh[26]={0};
            string s = words[i];
            for(j=0; j<s.length(); j++){
                if(tmpCh[s[j]-'a'] < ch[s[j]-'a'])
                    tmpCh[s[j]-'a']++;
                else
                    break;
            }
            if( j == s.length() ){
                ans+=words[i].size();
            }
        }
        return ans;
    }
};
