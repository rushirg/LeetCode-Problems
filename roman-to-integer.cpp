/*
 *Solution of problem 13
 *https://leetcode.com/problems/roman-to-integer/
 */


class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        for(int i=0; i<s.length();){
            if(s[i] == 'I' && s[i+1] != '\0' && s[i+1] == 'V'){
                sum += 4; i+= 2;
            }else if(s[i] == 'I' && s[i+1] != '\0' && s[i+1] == 'X'){
                sum += 9; i+= 2;
            }else if(s[i] == 'X' && s[i+1] != '\0' && s[i+1] == 'L'){
                sum += 40; i+= 2;
            }else if(s[i] == 'X' && s[i+1] != '\0' && s[i+1] == 'C'){
                sum += 90; i+= 2;
            }else if(s[i] == 'C' && s[i+1] != '\0' && s[i+1] == 'D'){
                sum += 400; i+= 2;
            }else if(s[i] == 'C' && s[i+1] != '\0' && s[i+1] == 'M'){
                sum += 900; i+= 2;
            }else if(s[i] == 'I'){
                sum += 1; i+=1;
            }else if(s[i] == 'V'){
                sum += 5; i+=1;
            }else if(s[i] == 'X'){
                sum += 10; i+=1;
            }else if(s[i] == 'L'){
                sum += 50; i+=1;
            }else if(s[i] == 'C'){
                sum += 100; i+=1;
            }else if(s[i] == 'D'){
                sum += 500; i+=1;
            }else if(s[i] == 'M'){
                sum += 1000; i+=1;
            }
        }
        return sum;
    }
};
