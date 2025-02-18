documentation for the methods in the `tree_traversal.py` file.

`inorder_tree_traversal`: Visit nodes in order (left subtree, root, right subtree)

`preorder_tree_traversal`: Visit nodes in preorder (root, left subtree, right subtree)

`postorder_tree_traversal`: Visit nodes in postorder (left subtree, right subtree, root)

`level_order_tree_traversal`: Visit nodes in level order, each level is visited from left to right.

Each traversal function:

- Takes an optional root node of type `TreeNode`
- Returns a list of node values in the specified order
- Uses iterative implementation to avoid recursion
- Includes full type hints for better IDE support

### Tree Node Interface

The library provides a flexible `TreeNode` class that can be used directly or as a reference implementation:

```python
@dataclass
class TreeNode:
    value: T
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
```

You can also use your own node implementations as long as they provide the required interface (value, left, and right attributes).
