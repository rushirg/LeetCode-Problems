/*
 *Solution for problem 476
 *https://leetcode.com/problems/number-complement/
 */
class Solution {
public:
    int findComplement(int num) {
        int bits = floor(log2(num)) + 1;
        return long(1 <<bits) - 1 ^ num;
    }
};
