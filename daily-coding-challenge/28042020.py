"""You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]

Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
"""
from collections import Counter, deque

class FirstUnique2:
    def __init__(self,nums):
        self.queue = nums

    def __str__(self):
        return str(self.queue)

    # time limit exceeded
    def showFirstUnique2(self):
        for num in self.queue:
            if self.queue.count(num) == 1:
                return num
        return -1 

    def showFirstUnique(self):
        visited = []
        for num in self.queue:
            if self.queue.count(num) == 1 and num not in visited:
                return num
            visited.append(num)
        return -1 

    def add(self,value):
        self.queue.append(value)
        
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.prev = None

class FirstUnique:
    def __init__(self,nums):
        self.head = ListNode(float('-inf'))
        self.tail = ListNode(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.seen = set()
        for num in nums:
            self.add(num)
    
    def add(self, num):
        if num not in self.seen:
            node = self.hasNode(num)
            if not node:
                insertNode = ListNode(num)
                temp = self.tail.prev
                # insert node
                insertNode.next = self.tail
                insertNode.prev = temp
                temp.next = insertNode
                self.tail.prev = insertNode
            else:
                self.removeNode(node)
                self.seen.add(num)
                
    def showFirstUnique(self):
        if self.head.next is self.tail:
            return -1
        else:
            return self.head.next.val
    
    def hasNode(self, num):
        runner = self.head.next
        while runner is not self.tail:
            if runner.val == num:
                return runner
            runner = runner.next
        return None
    
    def removeNode(self, node):
        preNode = node.prev
        nexNode = node.next
        preNode.next = nexNode
        nexNode.prev = preNode

class FirstUnique3:

    def __init__(self, nums: List[int]):
        self.cache = Counter(nums)
        self.uniques = deque(nums)
        
    def showFirstUnique(self) -> int:
        while self.uniques and self.cache[self.uniques[0]] != 1: 
            self.uniques.popleft()
        return self.uniques[0] if self.uniques else -1
        
    def add(self, value: int) -> None:
        self.cache[value] += 1
        self.uniques.append(value)
    
# q = FirstUnique([2,3,5])
# q.add(6)
# print(q)

# ["FirstUnique","add","add","add","add","add","showFirstUnique","add","showFirstUnique","add","add","add","add","add","add","add","showFirstUnique","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","showFirstUnique","showFirstUnique","add","showFirstUnique","showFirstUnique","add","add","showFirstUnique","showFirstUnique","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","showFirstUnique","add","add","add","add","showFirstUnique","add","add","add","add","add","add","add","add","add","add","add","add","add","showFirstUnique","add","add","showFirstUnique","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","add","showFirstUnique","add","add","showFirstUnique","add","add","showFirstUnique","add","add","add","add","add","add","add","add","add","add","add","add","showFirstUnique"]
test = [698,866,349,680,733,916,961,652,161,960,417,813,474,170,802,406,442,454,780,886,899,367,786,157,953,621,29,273,485,55,563,275,343,157,715,683,608,932,874,241,796,877,845,26,719,167,415,287,411,95,196,118,291,811,969,27,805,323,707,625,651,588,445,690,706,694,317,978,327,764,366,18,104,753,791,94,912,171,923,969,457,717,694,147,329,12,84,650,592,383,506,924,939,495,999,120,529,117,446,830,740,108,791,518,83,164,606,172,783,808]
# ],[657],[942],[901],[1000],[538],[],[390],[],[568],[608],[320],[508],[241],[360],[708],[],[182],[677],[591],[235],[890],[527],[294],[584],[747],[169],[342],[763],[246],[785],[76],[868],[177],[],[],[699],[],[],[342],[724],[],[],[973],[486],[814],[75],[697],[24],[454],[393],[667],[153],[490],[437],[536],[597],[794],[681],[],[338],[110],[360],[235],[],[541],[420],[399],[49],[444],[828],[583],[964],[39],[162],[896],[880],[456],[],[758],[442],[],[557],[100],[501],[863],[737],[621],[998],[637],[48],[88],[931],[146],[803],[109],[350],[859],[821],[875],[713],[260],[582],[230],[944],[173],[604],[498],[],[543],[33],[],[421],[413],[],[665],[722],[364],[306],[589],[1000],[338],[669],[477],[190],[665],[594],[]]
q = FirstUnique(test)
print(q.showFirstUnique())
# print(set(test))