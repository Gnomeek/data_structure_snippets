from typing import Dict, List, Optional


class Node:
    def __init__(self, val: str, children: Optional[Dict[str, List]] = None):
        self.val = val
        self.children = {} if children is None else children
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node("")
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.is_word = True
    
    def startswith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
    
    def search(self, word: str) -> bool:
        return self.searchIn(word, self.root)
        
    def searchIn(self, word, curr) -> bool:
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children and c != ".":
                return False
            if c == ".":
                for _, children in curr.children.items():
                    if self.searchIn(word[i+1:], children):
                        return True
                return False
            curr = curr.children[c]
        return curr.is_word