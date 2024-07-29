"""
OrderedDict

get o(1)  key, value
set o(1)
remove o(1)

key value
key -> hash function -> index list

incremental

[value, order]

1(1)  ,3 (3) , 4 (4)
key value 

items() [(k v), (k v)] o(n) | nlog(n)

o(n)
main list: [(1, 1), (3, 2), (2, 3), (4, 5)]
                | |
                 V
index list: [1, (3, 2), (2, 3), (4, 5)]


[
    hash(key) -> node
]

[node1, , node2, node3]

[
    (key, value),
    (key, value),

    (key, value),
]
"""


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node: Node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        if node == self.tail:
            if prev_node != None:
                prev_node.next = None
            self.tail = prev_node

        if node == self.head:
            if next_node != None:
                next_node.prev = None
            self.head = next_node

        if node != self.tail and node != self.head:
            if prev_node != None:
                prev_node.next = next_node
            if next_node != None:
                next_node.prev = prev_node

    def traverse(self):
        if self.head == None:
            return
        
        node = self.head
        while node != None:
            yield node
            node = node.next 


class OrderedDict:

    def __init__(self) -> None:
        # self.__size = 1000
        self.__key_node_dict = {}
        self.__linked_list = LinkedList()

    def set(self, key, value):
        # index = abs(hash(key)) % self.__size
        node = Node(key, value)
        self.__key_node_dict[key] = node
        self.__linked_list.add(node)

    def get(self, key, default_value=None):
        node = self.__key_node_dict.get(key)
        if node == None:
            return default_value
        
        return node.value
    
    def remove(self, key):
        node = self.__key_node_dict.get(key)
        if node == None:
            raise Exception("key is not in the dict")
        
        self.__key_node_dict.pop(key)
        self.__linked_list.remove(node)

    def items(self):
        for node in self.__linked_list.traverse():
            yield node.key, node.value


o = OrderedDict()
o.set("key1", "value1")
print(o.get("key1"))
# o.remove("key1")
# print(o.get("key1"))

for k ,v in o.items():
    print(k, v)





