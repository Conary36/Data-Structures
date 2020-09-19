"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return len(self.storage)
#
#     def enqueue(self, value):
#         return self.storage.insert(value)
#
#     def dequeue(self):
#        if len(self.storage) == 0:
#            return None
#         return self.storage.pop(0)
#
import sys

sys.path.append('./singly_linked_list/')
from singly_linked_list.singly_linked_list import Node, LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.front: LinkedList[Node] = None
        self.rear: LinkedList[Node] = None
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def is_empty(self) -> bool:
        """ returns boolean describing if queue is empty """
        return self.front is None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            assert isinstance(self.front, Node)
            node: Node = self.front
            self.front = node.next
            if self.front is None:
                self.rear = None
        return node.data
