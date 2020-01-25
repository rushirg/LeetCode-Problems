/*
Problem 5155. Rank Transform of an Array
https://leetcode.com/contest/biweekly-contest-18/problems/rank-transform-of-an-array/

Logic:
1. add the vector elements in set (for handeling duplicate elements and sorting)
2. iterate over set and add element in map with count as an rank (map will have all the unique elemets with their rank)
3. iterate over given vector arr and add values from map in the ans vector for each element in arr

Reference:
https://leetcode-cn.com/wnjxyk
*/

class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {

        set<int> s;
        map<int, int> m;
        int count = 0;

        for(auto i: arr)
            s.insert(i);

        for(auto j: s)
            m[j] = ++count;

        vector<int> ans;
        for(auto i: arr)
            ans.push_back(m[i]);
        return ans;
    }
};