/*
 *Solution for problem 700
 *https://leetcode.com/problems/search-in-a-binary-search-tree/
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {

        TreeNode *tmp = root;
        while(tmp!=NULL){
            if(tmp->val == val)
                return tmp;
            else if(tmp->val < val)
                tmp = tmp->right;
            else
                tmp = tmp->left;
        }
        return NULL;
    }
};
