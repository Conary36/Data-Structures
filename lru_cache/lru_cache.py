from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit # max number of nodes
        self.current = 0 # current number of spaces taken in the cache
        # self.cache = None # this will become the doubly linked list on the first set()
        self.cache = DoublyLinkedList()
        self.storage = {} # this would be another Data Structure that would store the encryption for the key and
        # probably encryption



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #  if key in self.storage:  # If the key is already in the storage
        #     pointer = self.cache.head  # pointer to point at the head
        #     while pointer is not None:  # As long as there is something at
        #         # the pointer
        #         if pointer.value == key:  # If the pointer value is the key...
        #             break  # Stop running the code
        #
        #         else:
        #             pointer = pointer.next  # Assign the pointer to point at
        #             # the next node
        #
        #     self.cache.move_to_front(pointer)  # Move the node that the
        #     # pointer is currently pointing at to the front (head) of the
        #     # linked list
        #     return self.storage[key]  # Returns the value in the storage at
        #     # the key
        #
        # else:  # If the key is not in the storage we did not find it.
        #     return None
        if key in self.storage:
            temp_node = self.storage[key]
            print(temp_node)
            self.cache.move_to_front(temp_node)
            return temp_node.value



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        if key in self.storage: # Check if the key is already in storage
            temp_node = self.storage[key] # Create a new node in the linked list
            # = temp_node # overwrites key with new value
            temp_node.value = value
            self.cache.move_to_front(temp_node) # Use the move to front method
            # in our doubly linked list class to move the temp node to the
            # front of the linked list
        else: # If key not already in the storage
            if self.current == self.limit: # When the current is the same as the limit
                removed_val = self.cache.remove_from_tail() # Remove the tail because that is the oldest value accessed
                self.current -= 1

                for k, v in self.storage.items():
                    if v.value == removed_val:
                        del self.storage[k] # This is where we actually remove the tail from the linked list
                        break
            temp_node = self.cache.add_to_head(value)
            # Now we can add the most recently used to the head of the linked list
            self.storage[key] = temp_node # add the value to the storage at the key
            self.current += 1
