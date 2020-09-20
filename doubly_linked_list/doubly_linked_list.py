"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def delete(self):
        if self.prev:
            self.next.prev = self.prev
        if self.next:
            self.prev.next = self.next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value)
        # add to empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # add to non-empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # update length
        self.length += 1



    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # find head node
        if self.head is None:
            return None

        else:
            ret_value = self.head.delete()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.tail.next = self.head
        self.head.prev = self.tail

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # don't need to return value

        # Do need to update head, tail
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:  # list has +2 nodes
            self.head = node.next
            node.delete()  # updating prev and/or next pointers
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    
    """

    def get_max(self):
        if not self.head:
            return None
        current = self.head
        max_val = current.value
        while current:
            if current.value < max_val:
                max_val = current.value
            current = current.next
        return max_val

    """
    Prints List
    """
    def print_doubly_list(self):
        print("this list has doubly elements:")
        ptr = self.head.next
        ptr2 = self.tail.prev
        while ptr or ptr2 is not None:
            print(ptr.get_value())
            print(ptr2.get_value())
            ptr = ptr.get_next_node()
            ptr2 = ptr2.get_next_node()

        print("End of list")