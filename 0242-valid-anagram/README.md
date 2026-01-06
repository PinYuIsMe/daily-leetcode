<h2><a href="https://leetcode.com/problems/valid-anagram">242. Valid Anagram</a></h2><h3>Easy</h3><hr><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;anagram&quot;, t = &quot;nagaram&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;rat&quot;, t = &quot;car&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

---

在 Python 中，**`str` (字串) 是不可變的 (Immutable)**，所以它沒有 `.sort()` 這個方法（`.sort()` 是 `list` 專用的原地排序方法）

#### 1. 使用 `sorted()` 函數 (推薦)

`sorted()` 可以接收任何序列（包括字串），並回傳一個**排序好的串列 (List)**。

```python
s = "anagram"
sorted_s = sorted(s) 
# sorted_s 會變成 ['a', 'a', 'a', 'g', 'm', 'n', 'r']

```
### 💡 教練深度解析：這題的三種解法

面試官通常會追問這題的複雜度，這裡有三種層次的回答：

| 解法 | 核心工具 | 時間複雜度 | 空間複雜度 | 備註 |
| --- | --- | --- | --- | --- |
| **排序法** | `sorted()` |  |  或  | 最快寫完，面試首選。 |
| **雜湊表** | `dict` 或 `Counter` |  | * | 效能最優（因為字母最多 26 個）。 |
| **陣列計數** | `[0] * 26` |  |  | 空間最省，展現底層理解。 |

> *註：雖然用了額外空間，但因為英文字母固定為 26 個，空間複雜度可以視為 。

---

### 🚀 進階挑戰：不用排序的  解法

如果你想給面試官留下印象，可以使用 `collections.Counter`：

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 直接比較兩個字串的字元頻率
        return Counter(s) == Counter(t)

```
