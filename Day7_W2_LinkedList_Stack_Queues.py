#************STACK***********
class Stack:
    def __init__(self):
        self.item=[]

    def push(self, data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        return None
            
    def is_empty(self):
        return len(self.item)==0
    
    def peek(self):
        return self.item[-1]
    
    def size(self):
        return len(self.item)

    def display(self):
        """Display stack contents from top to bottom"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Top")
        for items in reversed(self.item): 
            print(f"| {items} |")
        print("Bottom")
        

s=Stack()
s.push(3)
s.push(7)  
s.display() 
print(s.pop())
s.display()
s.push(8)
s.push(9)  
print(s.peek())
s.display()


#************QUEUE************ 
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.items:
            return None
        return self.items.popleft()
    
    def peek(self):
        if not self.items:
            return None
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  
print(q.peek())   
print(q.size())   

#********Linked List***********
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add to end of list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add to beginning of list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Remove first occurrence of data"""
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        """Print the entire list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)     
ll.append(20)     
ll.prepend(5)     
ll.delete(10)     
ll.display()     


#********LRU Cashe Problem********
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

print("=== LRU Cache Tests ===")
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))   
lru.put(3, 3)        
print(lru.get(2))    
lru.put(4, 4)       
print(lru.get(1))    
print(lru.get(3))     
print(lru.get(4))    

#********Reverse_List*************
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

print("\n=== Reverse Linked List Tests ===")
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original list:")
print_list(head)

reversed_head = reverse_list(head)
print("Reversed list:")
print_list(reversed_head) 

empty_head = None
print("Reversed empty list:")
print_list(reverse_list(empty_head))  