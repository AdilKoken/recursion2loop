# Tree Operations Documentation

This module provides essential binary tree operations implemented using iterative approaches instead of recursion. The methods are implemented in the [`tree_operations.py`](../recursion2loop/tree/tree_operations.py) file.

## Available Methods

- [`get_tree_height()`](#get_tree_height) - Calculate the height of a binary tree
- [`serialize_tree()`](#serialize_tree) - Convert a binary tree into a serialized list format
- [`deserialize_tree()`](#deserialize_tree) - Reconstruct a binary tree from its serialized format

## Detailed Documentation

### get_tree_height

Calculate the height (maximum depth) of a binary tree.

```python
def get_tree_height(root: Optional[TreeNode]) -> int
```

- **Parameters:**
  - `root`: Optional[TreeNode] - Root node of the binary tree
- **Returns:**
  - `int` - Height of the tree (0 for empty tree)
- **Details:**
  - Height is defined as the maximum depth of any leaf node
  - Depth is the number of edges from root to the node
  - Uses stack-based iteration to avoid recursion
  - Time complexity: O(n), where n is the number of nodes
  - Space complexity: O(h), where h is the height of the tree

### serialize_tree

Convert a binary tree into a serialized list format.

```python
def serialize_tree(root: Optional[TreeNode]) -> list[list[Optional[T]]]
```

- **Parameters:**
  - `root`: Optional[TreeNode] - Root node of the binary tree
- **Returns:**
  - `list[list[Optional[T]]]` - Serialized representation of the tree
- **Details:**
  - Uses level-order traversal for serialization
  - Format: First list contains root value, subsequent lists contain left and right child values
  - Optimizes space by removing trailing null values
  - Time complexity: O(n), where n is the number of nodes
  - Space complexity: O(w), where w is the maximum width of the tree

### deserialize_tree

Reconstruct a binary tree from its serialized format.

```python
def deserialize_tree(data: list[list[Optional[T]]]) -> Optional[TreeNode]
```

- **Parameters:**
  - `data`: list[list[Optional[T]]] - Serialized tree data
- **Returns:**
  - `Optional[TreeNode]` - Root node of the reconstructed tree
- **Details:**
  - Reconstructs tree using level-order traversal
  - Handles incomplete or optimized serialized data
  - Time complexity: O(n), where n is the number of nodes
  - Space complexity: O(w), where w is the maximum width of the tree

## Tree Node Interface

The operations work with the `TreeNode` class that implements this interface:

```python
@dataclass
class TreeNode[T]:
    value: T
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None
```

## Usage Example

```python
# Create a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Get tree height
height = get_tree_height(root)  # Returns 1

# Serialize the tree
serialized = serialize_tree(root)  # Returns [[1], [2, 3]]

# Deserialize back to tree structure
new_root = deserialize_tree(serialized)
```
