"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


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
        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # self.tail.next = self.head
    # self.head.prev = self.tail

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

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
        # If the list is empty do nothing
        if not self.head and not self.tail:
            return None
        # If list is only one node
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        # If the node is the HEAD node
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        # If the node is the TAIL node
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        # If the node is just an arbitrary node in the list
        else:
            self.length -= 1
            node.delete()

    """
    Finds and returns the maximum value of all the nodes
    in the List.

    """

    def get_max(self):
        if self.head is None:
            return None
        else:
            max_val = self.head.value
            current = self.head.next
            while current is not None:
                if current.value > max_val:
                    max_val = current.value
                current = current.next
            return max_val

    # def get_max(self):
    #     current_node = self.head
    #     max_value = self.head.value
    #     for i in range(1, self.length):
    #         current_node = current_node.next
    #         if current_node.value > max_value:
    #             max_value = current_node.value
    #     return max_value

    """
    Prints List
    """

    def print_doubly_list(self):
        print("this list has doubly elements:")
        ptr = self.head
        ret = ''
        while ptr is not None:
            # print(ptr.value)
            ret += str(ptr.value) + ' '
            ptr = ptr.next
        print(ret)

