class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # TODO
        if self.head is None:
            return None

        old_value = self.tail.get_value()
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return old_value
        else:
            current_node = self.head
            while current_node.get_next_node() is not self.tail:
                current_node = current_node.get_next_node()

            self.tail.set_next_node(None)
            self.tail = current_node
            return old_value

    def contains(self, value):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
            else:
                return False

    def get_max(self):
        # TODO
        if not self.head:
            return None
        current = self.head
        max_val = current.value
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next_node
        return max_val

    def add_to_sorted_list(self, value):

        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            if value <= self.head.get_value():
                self.add_to_head(value)
            else:
                # check if there is exacdtly one element
                if self.head == self.tail:
                    self.add_to_tail(value)
                else:
                    ptr = self.head

                    while ptr.get_value() <= value and ptr.get_next_node().get_value() <= value:
                        ptr = ptr.get_next_node()

                    if ptr == self.tail:

                        self.add_to_tail(value)
                    else:
                        new_node = Node(value)
                        new_node.set_next_node(ptr.get_next_node())
                        ptr.set_next_node(new_node)

    def print_list(self):
        print("this list has following elements:")
        ptr = self.head
        while ptr is not None:
            print(ptr.get_value())
            ptr = ptr.get_next_node()
        print("End of list")
        return
