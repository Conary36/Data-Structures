"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check for empty node to the left
        # if no node create one
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # repeat process for node to left, if not present, create node
                self.left.insert(value)
        # check if new node value is greater than or equal to new node value against self.value
        # after check value, repeat process for right side
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if self.value is target
        if self.value == target:
            # If yes return True,
            return True
        # If No:
        # go right
        elif self.value <= target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # Or go left
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right till you can not anymore
        # Return value at far right
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Lowest number is number to left
        # base case?
        if not self:
            return
        # recursive case?
        if self.left:
            self.in_order_print()
        print(self.value)
        if self.right:
            self.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)

        while len(queue) > 0:
            node = queue.dequeue()
            print(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    def dft_print(self):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            node = stack.pop()
            # call 'print()'
            print(node.value)
            # push its left and right children onto stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)

        if self.left is not None:
            self.left.pre_order_dft()
        if self.right is not None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
