from recursion2loop import tree_traversal

def test_inorder_tree_traversal():
    # Create a simple binary tree
    root = tree_traversal.TreeNode(1)
    root.left = tree_traversal.TreeNode(2)
    root.right = tree_traversal.TreeNode(3)

    # Perform inorder traversal and check result
    result = tree_traversal.inorder_tree_traversal(root)
    assert result == [2, 1, 3]

def test_preorder_tree_traversal():
    # Create a simple binary tree
    root = tree_traversal.TreeNode(1)
    root.left = tree_traversal.TreeNode(2)
    root.right = tree_traversal.TreeNode(3)

    # Perform preorder traversal and check result
    result = tree_traversal.preorder_tree_traversal(root)
    assert result == [1, 2, 3]  

def test_postorder_tree_traversal():
    # Create a simple binary tree
    root = tree_traversal.TreeNode(1)
    root.left = tree_traversal.TreeNode(2)
    root.right = tree_traversal.TreeNode(3)

    # Perform postorder traversal and check result
    result = tree_traversal.postorder_tree_traversal(root)
    assert result == [2, 3, 1]

def test_level_order_tree_traversal():
    # Create a simple binary tree
    root = tree_traversal.TreeNode(1)
    root.left = tree_traversal.TreeNode(2)
    root.right = tree_traversal.TreeNode(3)
    root.left.left = tree_traversal.TreeNode(4)
    root.left.right = tree_traversal.TreeNode(5)
    root.right.left = tree_traversal.TreeNode(6)
    root.right.right = tree_traversal.TreeNode(7)
    
    # Perform level order traversal and check result
    result = tree_traversal.level_order_tree_traversal(root)
    assert result == [1, 2, 3, 4, 5, 6, 7]
    
    
# check if it works with other data types, e.g. strings

def test_tree_traversals_with_other_data_types():
    # Create a simple binary tree with other data types
    root = tree_traversal.TreeNode("a")
    root.left = tree_traversal.TreeNode("b")
    root.right = tree_traversal.TreeNode("c")

    # Perform inorder traversal and check result
    result = tree_traversal.inorder_tree_traversal(root)
    assert result == ["b", "a", "c"]

    # Perform preorder traversal and check result
    result = tree_traversal.preorder_tree_traversal(root)
    assert result == ["a", "b", "c"]

    # Perform postorder traversal and check result
    result = tree_traversal.postorder_tree_traversal(root)
    assert result == ["b", "c", "a"]
    
    # Perform level order traversal and check result
    result = tree_traversal.level_order_tree_traversal(root)
    assert result == ["a", "b", "c"]


# check edge cases

def test_empty_tree():
    # Create an empty binary tree
    root = None

    # Perform inorder traversal and check result
    result = tree_traversal.inorder_tree_traversal(root)
    assert result == []

    # Perform preorder traversal and check result
    result = tree_traversal.preorder_tree_traversal(root)
    assert result == [] 

    # Perform postorder traversal and check result
    result = tree_traversal.postorder_tree_traversal(root)
    assert result == []

    # Perform level order traversal and check result
    result = tree_traversal.level_order_tree_traversal(root)
    assert result == []
    
def test_single_node_tree():
    # Create a single node binary tree
    root = tree_traversal.TreeNode(1)

    # Perform inorder traversal and check result
    result = tree_traversal.inorder_tree_traversal(root)
    assert result == [1]

    # Perform preorder traversal and check result
    result = tree_traversal.preorder_tree_traversal(root)
    assert result == [1]

    # Perform postorder traversal and check result
    result = tree_traversal.postorder_tree_traversal(root)
    assert result == [1]
    
    # Perform level order traversal and check result
    result = tree_traversal.level_order_tree_traversal(root)
    assert result == [1]

def test_tree_with_only_left_subtree():
    # Create a binary tree with only a left subtree
    root = tree_traversal.TreeNode(1)
    root.left = tree_traversal.TreeNode(2)
    root.left.left = tree_traversal.TreeNode(3)

    # Perform inorder traversal and check result
    result = tree_traversal.inorder_tree_traversal(root)
    assert result == [3, 2, 1]

    # Perform preorder traversal and check result
    result = tree_traversal.preorder_tree_traversal(root)
    assert result == [1, 2, 3]

    # Perform postorder traversal and check result
    result = tree_traversal.postorder_tree_traversal(root)
    assert result == [3, 2, 1]  
    
    # Perform level order traversal and check result
    result = tree_traversal.level_order_tree_traversal(root)
    assert result == [1, 2, 3]
    
def test_tree_with_only_right_subtree():
    # Create a binary tree with only a right subtree
    root = tree_traversal.TreeNode(1)
    root.right = tree_traversal.TreeNode(2)
    root.right.right = tree_traversal.TreeNode(3)

    # Perform inorder traversal and check result
    result = tree_traversal.inorder_tree_traversal(root)
    assert result == [1, 2, 3]

    # Perform preorder traversal and check result
    result = tree_traversal.preorder_tree_traversal(root)
    assert result == [1, 2, 3]

    # Perform postorder traversal and check result
    result = tree_traversal.postorder_tree_traversal(root)
    assert result == [3, 2, 1]
    
    # Perform level order traversal and check result
    result = tree_traversal.level_order_tree_traversal(root)
    assert result == [1, 2, 3]
    


    
def test_tree_with_complex_structure():
    # raw text comment, else / will give a warning
    r"""
    tree structure:
              1
            /   \
          2       3
         / \     / \
        4   5   6   7
       / \           \
      8   9           10
    """
    # Create a binary tree with a more complex structure
    root = tree_traversal.TreeNode(1)
    root.left = tree_traversal.TreeNode(2)
    root.right = tree_traversal.TreeNode(3)
    root.left.left = tree_traversal.TreeNode(4)
    root.left.right = tree_traversal.TreeNode(5)
    root.right.left = tree_traversal.TreeNode(6)
    root.right.right = tree_traversal.TreeNode(7)
    root.left.left.left = tree_traversal.TreeNode(8)
    root.left.left.right = tree_traversal.TreeNode(9)
    root.right.right.right = tree_traversal.TreeNode(10)
    
    # Perform inorder traversal and check result
    result = tree_traversal.inorder_tree_traversal(root)
    assert result == [8, 4, 9, 2, 5, 1, 6, 3, 7, 10]
    
    # Perform preorder traversal and check result
    result = tree_traversal.preorder_tree_traversal(root)
    assert result == [1, 2, 4, 8, 9, 5, 3, 6, 7, 10]

    # Perform postorder traversal and check result
    result = tree_traversal.postorder_tree_traversal(root)
    assert result == [8, 9, 4, 5, 2, 6, 10, 7, 3, 1]

    # Perform level order traversal and check result
    result = tree_traversal.level_order_tree_traversal(root)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
