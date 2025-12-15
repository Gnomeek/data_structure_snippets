from typing import Dict, Optional


class Node:
    def __init__(self, key, val, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append_to_head(self, node: Node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
    
    def move_to_head(self, node: Node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.append_to_head(node)

    def remove_tail(self):
        removed = self.tail.prev
        self.tail.prev = removed.prev
        removed.prev.next = self.tail
        return removed

class LruCache:
    def __init__(self, cap: int):
        self.memo: Dict[str, Node] = {}
        self.dll = DoublyLinkedList()
        self.cap: int = cap

    def get(self, key):
        if key in self.memo:
            node = self.memo[key]
            self.dll.move_to_head(node)
            return node.val
        else:
            return -1


    def put(self, key, value):
        if key in self.memo:
            node = self.memo[key]
            node.val = value
            self.dll.move_to_head(node)
        else:
            if len(self.memo) == self.cap:
                node = self.dll.remove_tail()
                del self.memo[node.key]
            node = Node(key, value)
            self.memo[key] = node
            self.dll.append_to_head(node)
