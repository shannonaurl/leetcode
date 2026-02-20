# class Node: 
#     def __init__(self, key, val):
#         self.key = key 
#         self.val = val 
#         self.prev = None 
#         self.next = None    


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.cap = capacity 
#         self.oldest = Node(0, 0)
#         self.latest = Node(0, 0)
#         self.oldest.next = self.latest 
#         self.latest.prev = self.oldest 
        

#     def get(self, key: int) -> int:
#         if key in cache: 
#             insert_node = cache[key]
#             insert_node.next.prev = insert_node.prev
#             insert_node.prev.next = insert_node.next 
#             temp = self.latest.prev
#             self.latest.prev = insert_node
#             insert_node.next = self.latest 
#             insert_node.prev = temp
#             temp.next = insert_node
#             return insert_node.val
#         else: 
#             return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in cache: 
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         insert_node = self.cache[key]
#         temp = self.latest.prev
#         self.latest.prev = insert_node
#         insert_node.next = self.latest 
#         insert_node.prev = temp
#         temp.next = insert_node

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)