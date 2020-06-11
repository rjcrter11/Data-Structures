from collections import deque

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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Check if value is less than the root
        # If yes, check if there is a left side
        # If not, create one
        # If yes, use insert recursively to add value into left side
        # Repeat for right side

        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if target is the root, if so, return true
        # If not, first check if its lesser
        # If so, check if there is a left node already
        # If not, return false. If so, use .contains recursively to find value
        # Repeat all checks for right side

        if target is self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Make variable for max value that is the root
        # Left side can be excluded
        # Check if right side exists
        # If yes, use get_max recursively on right side for max value
        # If no, max value is the root

        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call fn on root
        # If left exists, call fn recursively
        # If right exists, call fn recursively

        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Set a base case
        # Recursively print left side, then root, then right side
        if not node:
            return None
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Breadth first uses queue, so import
        # Append the given node to the queue
        # Loop through, popping off the first in line
        # Print current node in each iteration
        # Check left, then right and append each node to the queue to be printed
        queue = deque()
        queue.append(node)
        while len(queue) != 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Depth first uses a stack, use the same import, pop instead of popleft
        # Append the given node
        # Loop through, popping off the back of the stack
        # Print each node
        # Check left and right appending to the stack to be printed
        stack = deque()
        stack.append(node)
        while len(stack) != 0:
            current = stack.pop()

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # Set the base case - when something hits none
        # lol. According to the test file, print the root, then the left side, then right
        if not node:
            return None
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # NOTES:
    #       === Iterative pre order ===
    # def pre_order_dft_iterative(self, node):
    #     stack = deque()
    #     stack.append(node)
    #     while stack:
    #         current = stack.pop()
    #         print(current.value)
    #         if current.right:
    #             stack.append(current.right)
    #         if current.left:
    #             stack.append(current.left)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # Same as the other one, just print the root last
        if not node:
            return None
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)

    # NOTES:
    #       === Iterative post order ===
    # def post_order_dft_iterative(self, node):
    #     stack = deque()
    #     stack.append(node)
    #     root = deque()
    #     while stack:
    #         current = stack.pop()
    #         root.append(current.value)
    #         if current.left:
    #             stack.append(current.left)
    #         if current.right:
    #             stack.append(current.right)
    #     while root:
    #         print(root.pop())
