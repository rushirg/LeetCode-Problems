/*
 *Solution of problem 860
 *https://leetcode.com/problems/lemonade-change/
 */
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int change[3] = {0};
        for(int i=0; i<bills.size(); i++){

            if(bills[i] == 5){
                change[0]++;continue;
            }
            if(bills[i] == 10){
                change[1]++;
                change[0]--;
                if(change[0] < 0)
                    return false;
                continue;
            }
            if(bills[i] == 20){
                change[2]++;
                if(change[1] == 0){
                    if(change[0] >= 3){
                        change[0] -= 3;
                        continue;
                    }
                    else
                        return false;
                }
                change[1]--;
                change[0]--;
                if(change[0] < 0)
                    return false;
                continue;
            }
        }
        return true;
    }
};
