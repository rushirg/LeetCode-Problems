/*
 *Solution of problem 1290
 *https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 */

/*Multiply the result by 2(here, using bitwise operator) and add the node's data
 * Runtime: 0 ms
 * Memory: 8.3 MB
 *
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        ListNode* tmp = head;
        int sum = 0;
        while(tmp != NULL){
            sum = (sum << 1) + tmp->val;
            tmp = tmp->next;
        }
        return sum;
    }
};


/*Trivial approach:
 *1. Traverse the list and count the number of nodes
 *2. Traverse the list again from head but use the count for power function and calcuate the digit value
 *
 *Runtime: 8 ms
 *Memory: 8.5 MB
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 *
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        ListNode* tmp = head;
        int sum = 0, i = 0, val, count = -1;
        while(tmp != NULL){
            count += 1;
            tmp = tmp->next;
        }
        tmp = head;
        while(tmp != NULL){
            val = tmp->val;
            sum += (val * pow(2, count));
            count -= 1;
            tmp = tmp->next;
        }
        return sum;
    }
};
 *
 *
 *
 */
