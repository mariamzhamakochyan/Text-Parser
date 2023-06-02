class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.size
    
    def insert(self, key, val):
        idx = self.hash_func(key)
        node = self.table[idx]
        while node:
            if node.key == key:
                if val not in node.val:
                    node.val.append(val)  
                return
            node = node.next
        new_node = Node(key, [val])
        if self.table[idx] is None:
            self.table[idx] = new_node
        else:
            current = self.table[idx]
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, key):
        idx = self.hash_func(key)
        node = self.table[idx]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None
