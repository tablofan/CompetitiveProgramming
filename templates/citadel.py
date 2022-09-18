class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge Sort
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge_sort(head):
            if head is None or head.next is None: return head
            left = slow = fast = head
            fast = fast.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            left_sorted = merge_sort(left)
            right_sorted = merge_sort(right)
            return merge(left_sorted, right_sorted)

        def merge(l1, l2):
            dummy = ListNode()
            prev = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            prev.next = l1 or l2
            return dummy.next

        return merge_sort(head)

# Merge K sorted Lists
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next

# Online Election
def __init__(self, persons: List[int], times: List[int]):
    self.time = defaultdict(int)
    count = defaultdict(int)
    max_vote = [-1,-1]
    for i in range(len(persons)): #for each time in times, we calculate the leading person
        count[persons[i]] += 1
        if count[persons[i]] >= max_vote[1]:
            max_vote[0] = persons[i]
            max_vote[1] = count[persons[i]]
        self.time[times[i]] = max_vote[0]
    self.key = times #record the times list
    return
def q(self, t: int) -> int:
    index = bisect_right(self.key,t) #find the index for each t and return corresponding values
    return self.time[self.key[index-1]]

# Circular Queue
class MyCircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if (self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

# 2Sum 2
# Dict
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i,v in enumerate(numbers):
            if target - v in d:
                return [d[target-v]+1, i+1]
            d[v] = i
        return 'error'
# 2 Pointers
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1