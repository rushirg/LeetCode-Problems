/*
 *Solution of problem 237
 *https://leetcode.com/problems/delete-node-in-a-linked-list/
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
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};


/*
 * void deleteNode(ListNode* node) {
        *node = *node->next;
    }

*/



/*
 *
 *void deleteNode(ListNode* node) {
        ListNode* temp = node->next;
        node->val = temp->val;
        node->next = temp->next;
    }
 *
 */
