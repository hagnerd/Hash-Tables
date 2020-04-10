class Node:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"({self.key}, {self.value})"

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        node = Node(key, value)
        self.head = node

    def __str__(self):
        curr_node = self.head
        curr_val = f"{curr_node}"

        while curr_node.next is not None:
            curr_val += f" ->> {curr_node.next}"
            curr_node = curr_node.next

        return curr_val

    def insert(self, key, value):
        """
        Inserts the key at the last position in the LinkedPair
        """
        prev = self.head
        new_head = Node(key, value, prev)
        self.head = new_head
        return new_head

    def find_node(self, key):
        """
        Returns None or the found node with a given key
        """
        node = self.head
        found_node = None if node.key != key else node

        while node.next is not None and found_node is None:
            node = node.next
            if node is not None and node.key == key:
                found_node = node

        return found_node


    def upsert(self, key, value):
        """
        Inserts the key if it doesn't exist, or updates its value if it does
        """
        node = self.head
        found_key = node.key == key

        while not found_key and node.next is not None:
            node = node.next
            found_key = node.key == key

        if found_key:
            node.value = value
        else:
            self.insert(key, value)

    def remove(self, key):
        """
        Removes a node if it is found
        """
        curr = self.head
        prev = None

        while curr:
            if curr.key == key:
                if prev is not None:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return self.head
            prev = curr
            curr = curr.next

        return None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        hashed_key = self._hash_mod(key)

        new_node = LinkedPair(key, value)

        if self.storage[hashed_key] is not None:
            print("Collision occurred")
            self.storage[hashed_key].next = new_node
        else:
            self.storage[hashed_key] = value



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        hashed_key = self._hash_mod(key)

        node = self.storage[hashed_key]

        return self.storage[hashed_key]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
