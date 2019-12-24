/*
 *Solution of problem 258
 *https://leetcode.com/problems/add-digits/
 */

class Solution {
public:
    int addDigits(int num) {
        return (1 + (num - 1) % 9);
    }
};

/*
 *    int addDigits(int num) {
        int ans = 9;
        if(num == 0){
            ans = 0;
            return ans;
        }
        if(num%9 == 0 && num>0)
            return ans;
        else
            return(num%9);
    }
 *
 *More info: https://en.wikipedia.org/wiki/Digital_root
 * /
