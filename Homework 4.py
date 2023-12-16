Task 1:
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that come before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    # Add the merged interval
    result.append(new_interval)

    # Add intervals that come after new_interval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example 1
intervals1 = [[1, 3], [6, 9]]
new_interval1 = [2, 5]
output1 = insert_interval(intervals1, new_interval1)
print(output1)  # Output: [[1, 5], [6, 9]]

# Example 2
intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval2 = [4, 8]
output2 = insert_interval(intervals2, new_interval2)
print(output2)  # Output: [[1, 2], [3, 10], [12, 16]]

Task 2:

from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return []

    wordList.add(beginWord)

    # Build adjacency list
    adj_list = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            adj_list[pattern].append(word)

    # BFS to find the shortest transformation sequences
    queue = deque([(beginWord, [beginWord])])
    visited = set([beginWord])
    result = []

    while queue:
        current_word, path = queue.popleft()

        for i in range(len(current_word)):
            pattern = current_word[:i] + '*' + current_word[i+1:]
            neighbors = adj_list[pattern]

            for neighbor in neighbors:
                if neighbor == endWord:
                    result.append(path + [neighbor])
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

    return result

# Example 1
beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
output1 = findLadders(beginWord1, endWord1, wordList1)
print(output1)
# Output: [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]

# Example 2
beginWord2 = "hit"
endWord2 = "cog"
wordList2 = ["hot", "dot", "dog", "lot", "log"]
output2 = findLadders(beginWord2, endWord2, wordList2)
print(output2)
# Output: []

Task 3:

def maxProfit(prices):
    if not prices or len(prices) == 1:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
output1 = maxProfit(prices1)
print(output1)  # Output: 5

# Example 2
prices2 = [7, 6, 4, 3, 1]
output2 = maxProfit(prices2)
print(output2)  # Output: 0

Task 4:
def maxProfit(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        profit_today = prices[i] - prices[i-1]
        max_profit += max(0, profit_today)

    return max_profit

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
output1 = maxProfit(prices1)
print(output1)  # Output: 7

# Example 2
prices2 = [1, 2, 3, 4, 5]
output2 = maxProfit(prices2)
print(output2)  # Output: 4

# Example 3
prices3 = [7, 6, 4, 3, 1]
output3 = maxProfit(prices3)
print(output3)  # Output: 0

Task: 5
def maximumGap(nums):
    if len(nums) < 2:
        return 0

    min_num, max_num = min(nums), max(nums)
    bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
    bucket_count = (max_num - min_num) // bucket_size + 1

    buckets = [None] * bucket_count
    for num in nums:
        index = (num - min_num) // bucket_size
        if buckets[index] is None:
            buckets[index] = [num, num]
        else:
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

    max_gap = 0
    prev_max = min_num

    for bucket in buckets:
        if bucket is not None:
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]

    return max_gap

# Example 1
nums1 = [3, 6, 9, 1]
output1 = maximumGap(nums1)
print(output1)  # Output: 3

# Example 2
nums2 = [10]
output2 = maximumGap(nums2)
print(output2)  # Output: 0
