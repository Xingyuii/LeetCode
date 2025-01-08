class MyHashMap:
    def __init__(self):
        # Initialize the size of the hash map
        self.size = 1000
        # Create an array of linked lists (buckets) to store key-value pairs
        self.buckets = [None] * self.size

    def _hash(self, key):
        # Hash function to map a key to an index in the buckets array
        return key % self.size

    def put(self, key, value):
        # Find the index of the bucket where the key-value pair should be stored
        index = self._hash(key)
        if self.buckets[index] is None:
            # If the bucket is empty, create a new node and store the key-value pair
            self.buckets[index] = ListNode(key, value)
        else:
            # If the bucket is not empty, traverse the linked list
            curr = self.buckets[index]
            while True:
                if curr.key == key:
                    # If the key already exists, update the value
                    curr.val = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            # If the key does not exist, append a new node at the end of the linked list
            curr.next = ListNode(key, value)

    def get(self, key):
        # Find the index of the bucket where the key might be stored
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            # Traverse the linked list to find the key
            if curr.key == key:
                return curr.val
            curr = curr.next
        # If the key is not found, return -1
        return -1

    def remove(self, key):
        # Find the index of the bucket where the key might be stored
        index = self._hash(key)
        curr = self.buckets[index]
        if curr is None:
            return
        if curr.key == key:
            # If the key is at the head of the linked list, remove the head
            self.buckets[index] = curr.next
            return
        while curr.next:
            if curr.next.key == key:
                # If the key is found, remove the node
                curr.next = curr.next.next
                return
            curr = curr.next


class ListNode:
    def __init__(self, key, val):
        # Constructor for ListNode, which stores a key-value pair
        self.key = key
        self.val = val
        # Pointer to the next node in the linked list
        self.next = None