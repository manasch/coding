[[389] - Find the Difference](https://leetcode.com/problems/find-the-difference)

---

- Easy
- [Submission](https://leetcode.com/problems/find-the-difference/submissions/1058412448/)
- [Submission](https://leetcode.com/problems/find-the-difference/submissions/1058413738/)
- hash-table, string, bit-manipulation, sorting

---

## Problem Statement

<p>You are given two strings <code>s</code> and <code>t</code>.</p>

<p>String <code>t</code> is generated by random shuffling string <code>s</code> and then add one more letter at a random position.</p>

<p>Return the letter that was added to <code>t</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, t = &quot;abcde&quot;
<strong>Output:</strong> &quot;e&quot;
<strong>Explanation:</strong> &#39;e&#39; is the letter that was added.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;, t = &quot;y&quot;
<strong>Output:</strong> &quot;y&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 1000</code></li>
	<li><code>t.length == s.length + 1</code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>


---

## Solution

```cpp
class Solution {
public:
    char findTheDifference(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != t[i]) {
                return t[i];
            }
        }
        return t.back();
    }
};
```

```cpp
class Solution {
public:
    char findTheDifference(string s, string t) {
        char res = 0;
        for (char chr: s + t) {
            res ^= chr;
        }
        return res;
    }
};
```

---

## Notes

- Implemented the first thing that came to mind, which is, sort them and the first time there is a mismatch, return the character from t.
- But a faster method would be to just XOR all characters in both the strings, and the extra character would remain.
