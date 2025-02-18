from typing import Optional
from .tree_node import TreeNode, validate_tree_node, T
from .tree_traversal import level_order_tree_traversal

# Now you can add your tree operations here
# For example:

def get_tree_height(root: Optional[TreeNode]) -> int:
    """
    Calculate the height of the binary tree.

    The height of a binary tree is defined as the maximum depth of any leaf node in the tree.
    Depth is defined as the number of edges on the path from the root to the node.
    The height of an empty tree is 0.

    Args:
        root: Root node of the binary tree.

    Returns:
        Height of the tree (0 for an empty tree).
    """
    # If the tree is empty, its height is 0
    if not root:
        return 0

    validate_tree_node(root)

    # Initialize a stack with a tuple containing the root node and its depth (0)
    stack = [(root, 0)]
    max_height = 0

    while stack:
        node, depth = stack.pop()  # Retrieve the current node and its depth
        max_height = max(max_height, depth)

        # If the current node has a right child, add it to the stack with incremented depth
        if node.right:
            stack.append((node.right, depth + 1))
        # If the current node has a left child, add it to the stack with incremented depth
        if node.left:
            stack.append((node.left, depth + 1))

    return max_height

def serialize_tree(root: Optional[TreeNode]) -> list[list[Optional[T]]]:
    """
    Serialize the binary tree into a list for later deserialization.

    Serialization converts the tree structure into a linear format (list) using 
    level order traversal (breadth-first traversal).

    The first element of the list is a list of one element, the root node
    The rest of the elements are lists of two, representing the left and right children of each node.
    If a node is null, the corresponding position in the list is None.

    Args:
        root: Root node of the binary tree.

    Returns:
        A list of lists of node values representing the serialized binary tree.
        The first element is the root node, followed by the left and right children of the non-null nodes.
        Returns an empty list if the tree is empty.
    """
    # If the tree is empty, return an empty list
    if not root:
        return []

    # Ensure the root node is a valid TreeNode
    validate_tree_node(root)

    queue = [root]  # Initialize the queue with the root node for level order traversal
    serialized_tree = [[root.val]]  # Start serialization with the root node's value

    while queue:
        node = queue.pop(0)

        # Retrieve the value of the child, or None if it doesn't exist
        left_val = node.left.val if node.left else None
        right_val = node.right.val if node.right else None

        serialized_tree.append([left_val, right_val])

        # If the child exists, enqueue it for further processing
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return serialized_tree  # Return the fully serialized tree

def deserialize_tree(data: list[list[Optional[T]]]) -> Optional[TreeNode]:
    """
    Deserialize a list back into a binary tree structure.

    Args:
        data: A list of lists of node values produced by the serialize_tree function.

    Returns:
        The root node of the reconstructed binary tree.
        Returns None if the input list is empty.
    """
    # If the input data is empty, return None to represent an empty tree
    if not data:
        return None

    # Create the root node from the first element in the data
    root = TreeNode(data[0][0])
    queue = [root]

    index = 1

    while queue and index < len(data):
        node = queue.pop(0)

        # If the child exists, create it and enqueue it for further reconstruction
        if data[index][0] is not None:
            node.left = TreeNode(data[index][0])
            queue.append(node.left)

        if data[index][1] is not None:
            node.right = TreeNode(data[index][1])
            queue.append(node.right)

        index += 1

    return root
