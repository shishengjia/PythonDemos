import heapq

nums = [1, 7, 3, 22, -3, 9]
# 最大和最小的三个数
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


# 还可以接受一个参数key，处理更复杂的数据
records = [
    {'name': 'Tom', 'score': 40},
    {'name': 'Jack', 'score': 60},
    {'name': 'Marry', 'score': 55},
    {'name': 'Boen', 'score': 30},
    {'name': 'Alex', 'score': 58},
]
print(heapq.nlargest(3, records, key=lambda x:x['score']))
print(heapq.nsmallest(3, records, key=lambda x:x['score']))

# 堆最重要的特性就是heap[0]总是最小的那个元素
heap = nums
heapq.heapify(heap)
# 使用下表找到最小的三个元素，也可以使用heappop方法依次找到
print(heap[0], heap[1], heap[2])
for x in range(3):
    print(heapq.heappop(heap), end=',')

"""
具体情况看使用场景，详情查看PythonCookBook第8页
"""
