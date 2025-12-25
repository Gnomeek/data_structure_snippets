from typing import Dict, List
class Node:
    def __init__(self):
        self.children = {}
        self.name = None
        self.is_file = False
        self.content = []

class Tree:
    def __init__(self):
        self.root = Node()
    
    def push(self, path, is_file):
        curr = self.root
        parts = path.split("/")
        for p in parts[1:]:
            if p not in curr.children:
                curr.children[p] = Node()
            curr = curr.children[p]
        curr.is_file = is_file
        if is_file:
            curr.name = parts[-1]
        return curr

    def search(self, path):
        curr = self.root
        if path == "/":
            return curr
        parts = path.split("/")
        for p in parts[1:]:
            if p not in curr.children:
                return None
            curr = curr.children[p]
        return curr



class FileSystem:
    def __init__(self):
        self.trie = Tree()

    def ls(self, path) -> List[str]:
        node = self.trie.search(path):
        if not node:
            return []
        if node.is_file:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path):
        self.trie.push(path)

    def addContentToFile(self, file_path: str, content: str):
        node = self.trie.push(file_path, True)
        node.content.append(content)

    def readContentFromFile(self, file_path: str) -> str:
        node = self.trie.search(file_path)
        return "".join(node.content)