from typing import Optional

# Binary Tree
class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root: Optional[TreeNode]):
    res = []
    if not root:
        return res
    stack = []
    while stack or root:
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        curr = stack.pop()
        root = curr.right
    return res

def inorder_traversal(root: Optional[TreeNode]):
    res = []
    if not root:
        return res
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        curr = stack.pop()
        res.append(curr.val)
        root = curr.right

def postorder_traversal(root: Optional[TreeNode]):
    res = []
    if not root:
        return res
    stack = []
    prev = None
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        curr = stack.pop()
        if not curr.right or curr.right == prev:
            res.append(curr.val)
            prev = curr
            root = None
        else:
            stack.append(curr)
            root = curr.right
    return res


def levelorder_traversal(root: Optional[TreeNode]):
    res = []
    if not root:
        return res
    queue = [root]
    while queue:
        size = len(queue)
        curr_level = []
        next_level = []
        for _ in range(size):
            curr = queue.pop(0)
            curr_level.append(curr.val)
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)
        queue = next_level
        res.append(curr_level)
    return res
