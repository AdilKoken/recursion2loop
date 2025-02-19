# Tree Traversal Documentation

This module provides various binary tree traversal methods implemented iteratively. The methods are implemented in the [`tree_traversal.py`](../recursion2loop/tree/tree_traversal.py) file.

## Available Methods

- [`inorder_tree_traversal()`](#inorder_tree_traversal) - Visit nodes in order (left → root → right)
- [`preorder_tree_traversal()`](#preorder_tree_traversal) - Visit nodes in preorder (root → left → right)
- [`postorder_tree_traversal()`](#postorder_tree_traversal) - Visit nodes in postorder (left → right → root)
- [`level_order_tree_traversal()`](#level_order_tree_traversal) - Visit nodes level by level, left to right

## Detailed Documentation

### inorder_tree_traversal

Visit nodes in order (left subtree → root → right subtree).

```python
def inorder_tree_traversal(root: Optional[TreeNode]) -> list[T]
```

- **Parameters:**
  - `root`: Optional[TreeNode] - Root node of the binary tree
- **Returns:**
  - `list[T]` - List of node values in inorder sequence
- **Details:**
  - Uses stack-based iteration
  - Time complexity: O(n)
  - Space complexity: O(h), where h is tree height

### preorder_tree_traversal

Visit nodes in preorder (root → left subtree → right subtree).

```python
def preorder_tree_traversal(root: Optional[TreeNode]) -> list[T]
```

- **Parameters:**
  - `root`: Optional[TreeNode] - Root node of the binary tree
- **Returns:**
  - `list[T]` - List of node values in preorder sequence
- **Details:**
  - Uses stack-based iteration
  - Time complexity: O(n)
  - Space complexity: O(h)

### postorder_tree_traversal

Visit nodes in postorder (left subtree → right subtree → root).

```python
def postorder_tree_traversal(root: Optional[TreeNode]) -> list[T]
```

- **Parameters:**
  - `root`: Optional[TreeNode] - Root node of the binary tree
- **Returns:**
  - `list[T]` - List of node values in postorder sequence
- **Details:**
  - Uses stack-based iteration
  - Time complexity: O(n)
  - Space complexity: O(h)

### level_order_tree_traversal

Visit nodes level by level, left to right.

```python
def level_order_tree_traversal(root: Optional[TreeNode]) -> list[T]
```

- **Parameters:**
  - `root`: Optional[TreeNode] - Root node of the binary tree
- **Returns:**
  - `list[T]` - List of node values in level-order sequence
- **Details:**
  - Uses queue-based iteration
  - Time complexity: O(n)
  - Space complexity: O(w), where w is maximum tree width

## Tree Node Interface

```python
@dataclass
class TreeNode[T]:
    value: T
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
```

## Usage Example

```python
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

inorder = inorder_tree_traversal(root)      # [2, 1, 3]
preorder = preorder_tree_traversal(root)    # [1, 2, 3]
postorder = postorder_tree_traversal(root)  # [2, 3, 1]
levelorder = level_order_tree_traversal(root) # [1, 2, 3]
```

## Visual Representation

```
         1
        / \
       2   3
      / \   \
     4   5   6

Traversal Results:
- Inorder:     [4, 2, 5, 1, 3, 6]
- Preorder:    [1, 2, 4, 5, 3, 6]
- Postorder:   [4, 5, 2, 6, 3, 1]
- Level-order: [1, 2, 3, 4, 5, 6]
```
