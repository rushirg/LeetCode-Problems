/*
 * Solution of problem 1281
 *https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
 */

class Solution {
public:
    int subtractProductAndSum(int n) {
        int tmp = n, sum = 0, prod = 1, dig;
        while(tmp > 0){
            dig = tmp % 10;
            tmp /= 10;
            sum += dig;
            prod *= dig;
        }
        return prod - sum;
    }
};
