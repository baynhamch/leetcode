

## 🧠 1. String & Two-Pointer Helpers
Expand Around Center

``` Python
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]
```

Reverse a String / Substring
``` Python
def reverse_str(s, left, right):
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)
```

Check if Palindrome
``` Python
def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]
```

Sliding Window Pattern
``` Python
def sliding_window(s, k):
    left = 0
    seen = {}
    for right, ch in enumerate(s):
        # Add new character
        seen[ch] = seen.get(ch, 0) + 1
        
        # Shrink window if condition fails
        while len(seen) > k:
            seen[s[left]] -= 1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left += 1
```


## 🧮 2. Array & Math Helpers

Two-Pointer Sum
``` Python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
```

Prefix Sum
``` Python
def prefix_sum(nums):
    prefix = [0]
    for n in nums:
        prefix.append(prefix[-1] + n)
    return prefix
```

Kadane’s Algorithm (max subarray sum)
``` Python
def max_subarray(nums):
    cur = best = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best
```

Binary Search (generic)
``` Python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 🧱 3. HashMap / Counting Helpers

Frequency Counter
``` Python
from collections import Counter
freq = Counter(s)
```

 Check Anagrams
``` Python
from collections import Counter
freq = Counter(s)
```

## 🌲 4. Tree Helpers

norder Traversal (Recursive)
``` Python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

Level Order (BFS)
``` Python
from collections import deque
def level_order(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

## 🔁 5. Recursion & Backtracking Helpers

Permutations
``` Python
def backtrack(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)
```

Subsets
``` Python
def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res
```

Graph / BFS / DFS Templates
``` Python
def dfs(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1':
        return
    grid[r][c] = '0'
    dfs(grid, r+1, c)
    dfs(grid, r-1, c)
    dfs(grid, r, c+1)
    dfs(grid, r, c-1)
```

BFS (queue)
``` Python
from collections import deque
def bfs(start):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```
## Heap / Priority Queue Helper


``` Python
import heapq

def top_k(nums, k):
    return heapq.nlargest(k, nums)
```
## 🧩 8. Dynamic Programming Template
``` Python
def dp_template(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] + dp[i-2]  # example relation
    return dp[n]
```


Category
Function
Common Problem Types
String
expand(), is_palindrome()
Palindromes, substring checks
Array
two_sum_sorted(), max_subarray()
2-pointer, sliding window
Search
binary_search()
Sorted arrays, rotations
Counting
Counter, is_anagram()
Frequency, uniqueness
Trees
inorder(), level_order()
Traversals, validation
Graph
dfs(), bfs()
Islands, shortest paths
DP
dp_template()
Stairs, knapsack
Backtrack
subsets(), backtrack()
Permutations, combinations
