"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"Value: {self.value} | Prev: {self.prev} | Next: {self.next}"

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        return f"Head: {self.head} | Tail: {self.tail} | Length: {self.length} "

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value, None, None)
        # either will add 1 to self.length
        self.length += 1
        # 1st, check if the DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            # new node's next pointer goes to original head
            # original prev points at new node
            # original head is set as head of new node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # switched to using the delete method in DLL
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # similar to head, just use the tail
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # switched to using delete method on DLL
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # Check for empty list
        if not self.head:
            return None
        # Check that its not already the head
        if node is self.head:
            return None
        # Else, can use add_to_head method and delete from ListNode from  to remove node from current spot
        else:
            self.add_to_head(node.value)
            self.delete(node)  # lol delete from dll is better

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # Similar to move to front
        # Check that it's not empty or tail
        # Else, use add_to_tail and delete methods
        if not self.head:
            return None
        if node is self.tail:
            return None
        else:
            self.add_to_tail(node.value)
            self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # Check for empty
        if not self.head and not self.tail:
            return None
        # Handles decrementing
        self.length -= 1
        # Check for single node list
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # Check if node is the head of the list
        elif self.head is node:
            self.head = self.head.next
            node.delete()
        # Check if node is the tail of the list
        elif self.tail is node:
            self.tail = self.tail.prev
            node.delete()
        # Just delete if it's not
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # Check for empty DLL
        # Variable(current) for head and its value(max) to loop through
        # While loop that goes til you hit None
        # When the max is less than the current value -- set it to max
        if self.length == 0:
            return None
        else:
            current = self.head
            max_value = self.head.value
            while current.next is not None:
                current = current.next
                if current.value > max_value:
                    max_value = current.value
            return max_value

