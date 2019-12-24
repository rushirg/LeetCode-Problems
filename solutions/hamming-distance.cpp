/*
 *Solution for problem 461
 *https://leetcode.com/problems/hamming-distance/
 */
class Solution {
public:
    int bitCount(int n){
        int count = 0;
        while(n){
            count += n & 1;
            n >>= 1;
        }
        return count;
    }

    int hammingDistance(int x, int y) {
        int newNum = x ^ y;
        return bitCount(newNum);
    }
};
