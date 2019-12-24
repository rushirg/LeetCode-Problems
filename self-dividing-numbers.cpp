/*
 *Solution for problem 728
 *https://leetcode.com/problems/self-dividing-numbers/
 */
class Solution {
public:
    bool checkNum(int n){
        int tmp = n, rem;
        while(tmp > 0){
            rem = tmp % 10;
            if(rem == 0 || n % rem != 0)
                return false;
            tmp /= 10;
        }
        return true;
    }

    vector<int> selfDividingNumbers(int left, int right) {

        vector<int> ans;
        for(int i=left; i<=right; i++){
            if(checkNum(i))
                ans.push_back(i);
        }
        return ans;
    }
};
