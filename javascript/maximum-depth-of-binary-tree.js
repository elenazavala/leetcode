/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = (root) => {
    let maxDepth = 0;
    let dfs = (node, depth) => 
    {
        if (!node){
          return maxDepth;
        }
        if (depth > maxDepth){
          maxDepth = depth;
        }
        dfs(node.right, depth + 1);
        dfs(node.left, depth + 1);
    }
    dfs(root, 1);
    return maxDepth;
};
