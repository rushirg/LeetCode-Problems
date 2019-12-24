/*
Solution for problem 595
https://leetcode.com/problems/big-countries/
*/
# Write your MySQL query statement below
SELECT name, population, area FROM World Where population > 25000000 OR area > 3000000
