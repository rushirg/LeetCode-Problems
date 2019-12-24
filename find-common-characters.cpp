/*
 *Solution for problem 1002
 *https://leetcode.com/problems/find-common-characters/
 */
class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        int count[100][26] = {0};
        for (int i = 0; i < A.size(); ++i) {
            for (auto ch: A[i]) {
                count[i][ch - 97]++;
            }
        }
        vector<string> result;
        for (int i = 0; i < 26; ++i) {
            int k = INT_MAX;
            for (int j = 0; j < A.size(); j++) {
                if (count[j][i] == 0) {
                    k = -1;
                    break;
                }
                k = min(k, count[j][i]);
            }
            while (k -- > 0) {
                result.push_back(string(1, (char)(97 + i)));
            }
        }
        return result;
    }
};
