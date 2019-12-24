/*
 *Solution of problem 1009
 *https://leetcode.com/problems/complement-of-base-10-integer/
 */
class Solution {
public:
    int bitwiseComplement(int N) {
        if(N == 0)
            return 1;
        unsigned int numberOfBits = floor(log2(N))+1;
        return((1 << numberOfBits)-1) ^ N;
    }
};
