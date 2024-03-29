[[572] - Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree)

---

- Easy
- [Submission](https://leetcode.com/problems/subtree-of-another-tree/submissions/983090486/)
- tree, depth-first-search, string-matching, binary-tree, hash-function

---

## Problem Statement

<p>Given the roots of two binary trees <code>root</code> and <code>subRoot</code>, return <code>true</code> if there is a subtree of <code>root</code> with the same structure and node values of<code> subRoot</code> and <code>false</code> otherwise.</p>

<p>A subtree of a binary tree <code>tree</code> is a tree that consists of a node in <code>tree</code> and all of this node&#39;s descendants. The tree <code>tree</code> could also be considered as a subtree of itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 532px; height: 400px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 502px; height: 458px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the <code>root</code> tree is in the range <code>[1, 2000]</code>.</li>
	<li>The number of nodes in the <code>subRoot</code> tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= root.val &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= subRoot.val &lt;= 10<sup>4</sup></code></li>
</ul>


---

## Solution

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool sameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL) {
            return true;
        }
        if ((p == NULL || q == NULL) || (p->val != q->val)) {
            return false;
        }

        return (sameTree(p->left, q->left) && sameTree(p->right, q->right));
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (subRoot == NULL) {
            return true;
        }
        if (root == NULL) {
            return false;
        }

        if (sameTree(root, subRoot)) {
            return true;
        }
        else {
            return (isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot));
        }
    }
};
```

---

## Notes

- Personally don't think this should be an `easy` problem but whatever.
- Traverse using dfs or bfs and at each node check if the subtree is the same tree with the current node as root.
- Apply the same algo used for same tree as in `LC100`.
