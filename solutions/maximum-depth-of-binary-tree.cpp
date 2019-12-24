/*
 *Soultion of problem 104
 *https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    int maxDepth(TreeNode* root) {
        if(root == NULL)
            return 0;
        int leftMax = maxDepth(root->left);
        int rightMax = maxDepth(root->right);
        return max(leftMax, rightMax) + 1;
    }
};
