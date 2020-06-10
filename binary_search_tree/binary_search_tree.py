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

    def __repr__(self):
        return f"Value: {self.value} \nLeft: {self.left} \nRight: {self.right}"

    # Insert the given value into the tree
    def insert(self, value):

        # TODO:
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

        # TODO:
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
        # TODO:
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
        # TODO:
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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


arr = []
def fn(x): return arr.append(x)


bst = BSTNode(8)
bst.insert(4)
bst.insert(12)
bst.insert(2)
bst.insert(14)
bst.insert(6)
bst.insert(10)
bst.insert(1)
bst.insert(15)
bst.insert(3)
bst.insert(13)
bst.insert(5)
bst.insert(11)
bst.insert(7)
bst.insert(9)
print(bst.contains(12))
print(bst.contains(16))
print(bst.get_max())
bst.for_each(fn)
print(arr)
