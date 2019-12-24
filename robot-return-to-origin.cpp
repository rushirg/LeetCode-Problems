/*
 *Solution for problem 657
 *https://leetcode.com/problems/robot-return-to-origin/
 */
class Solution {
public:
    bool judgeCircle(string moves) {
        int arr[4]={0};
        for(int i=0; i<moves.length(); i++){
            if(moves[i] == 'R')
                arr[0]++;
            else if(moves[i] == 'L')
                arr[1]++;
            else if(moves[i] == 'U')
                arr[2]++;
            else
                arr[3]++;
        }
        return (abs(arr[0]-arr[1]) == 0 && abs(arr[2] - arr[3] == 0));
    }
};
