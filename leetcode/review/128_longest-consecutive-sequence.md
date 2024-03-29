[[128] - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence)

---

- Medium
- [Submission](https://leetcode.com/problems/longest-consecutive-sequence/submissions/879172294/)
- array, hash-table, union-find

---

## Problem Statement

<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // unordered_set<int> hashSet(nums.begin(), nums.end());
        // int longest = 0;
        // int temp;

        // if (nums.size() == 0) return 0;

        // for (int x: nums) {
        //     temp = 1;
        //     while (hashSet.count(x - 1 - temp)) {
        //         ++temp;
        //     }
        //     longest = max(temp, longest);
        // }
        // return longest;
        unordered_set<int> hashSet(nums.begin(), nums.end());
        int longest = 0;
        int temp;

        for (int x: nums) {
            if (!hashSet.count(x + 1)) {
                temp = 1;
                while (hashSet.count(x - temp))
                    ++temp;
                
                longest = max(temp, longest);
            }
        }
        return longest;
    }
};
```

---

## Notes

- Generate a hashset (which is basically a set whose elements can be hashed so searching is `O(n)`).
- Iterate through every number in the nums array, for every number we just check if it is the last number in the sequence, this can be done by checking if a number after it exists. If it does, we keep going back till the number doesn't exist and stop the loop, This won't iterate n times for each number in the average case.
