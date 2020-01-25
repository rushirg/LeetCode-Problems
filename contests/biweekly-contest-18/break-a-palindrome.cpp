/*
1328. Break a Palindrome
https://leetcode.com/contest/biweekly-contest-18/problems/break-a-palindrome/

Logic:
1. check the size of string is 1, if it is return ""
2. loop over to the mid of string and check if character is not equal to 'a' if not update with 'a' and return string
3. If the string has 'a' till its mid, loop from last element of string and check if it is less than 'z' if it is next character
Another way for the 3rd step is to update the last element of the string with 'b' as first char of string is a which makes non palindrom string

Reference:
https://leetcode-cn.com/eastfront
*/

class Solution {
public:
    string breakPalindrome(string palindrome) {

        int n = palindrome.size();

        if(n == 1)
            return "";

        int m = n/2, i;

        for(i=0; i<m; i++){
            if(palindrome[i] != 'a'){
                palindrome[i] = 'a';
                return palindrome;
            }
        }

        for(i = n - 1; i>=0; i--){
            if(palindrome[i] < 'z'){
                palindrome[i]++;
                return palindrome;
            }
        }

        return "";

    }
};