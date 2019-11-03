/*
 *Solution for problem 69
 *https://leetcode.com/problems/sqrtx/
 */

class Solution {
public:
    int mySqrt(int x) {
        if(x == 0 || x == 1)
            return x;
        long start = 0, end = x/2, mid, ans;
        while(start<=end){
            mid = (start + end) / 2;

            if(mid * mid == x)
                return mid;
            if(mid * mid < x){
                start = mid + 1;
                ans = mid;
            }
            else
                end = mid - 1;
        }
        return ans;
    }
};
