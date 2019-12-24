/*
 *Solution of problem 387 
 *https://leetcode.com/problems/first-unique-character-in-a-string/
 */
class Solution {
public:
    int firstUniqChar(string s) {
        int size = s.size(), arr[26] = {0};
        for(int i=0; i<size; i++)
            arr[s[i] - 'a']++;
        for(int i=0; i<size; i++){
            if(arr[s[i] - 'a'] == 1)
                return i;
        }
        return -1;
    }
};
