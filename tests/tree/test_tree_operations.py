"""
Test the tree operations module
"""

from recursion2loop import tree_operations


# test get_tree_height
class TestGetTreeHeight:
    """
    Test the get_tree_height function
    """

    def test_get_tree_height_classic_small_tree(self):
        """
        Test the get_tree_height function with a classic small binary tree
        """
        # Create a simple binary tree
        root = tree_operations.TreeNode(1)
        root.left = tree_operations.TreeNode(2)
        root.right = tree_operations.TreeNode(3)

        # Calculate the height of the tree
        height = tree_operations.get_tree_height(root)

        # Check if the height is correct
        assert height == 1

    def test_get_tree_height_empty_tree(self):
        """
        Test the get_tree_height function with an empty binary tree
        """
        # Create an empty binary tree
        root = None

        # Calculate the height of the tree
        height = tree_operations.get_tree_height(root)

        # Check if the height is correct
        assert height == 0

    def test_get_tree_height_single_node_tree(self):
        """
        Test the get_tree_height function with a single node binary tree
        """
        # Create a single node binary tree
        root = tree_operations.TreeNode(1)

        # Calculate the height of the tree
        height = tree_operations.get_tree_height(root)

        # Check if the height is correct
        assert height == 0

    def test_get_tree_height_complex_tree_1(self):
        """
        Test the get_tree_height function with a complex binary tree
        """
        # Create a complex binary tree
        root = tree_operations.TreeNode(1)
        root.left = tree_operations.TreeNode(2)
        root.right = tree_operations.TreeNode(3)
        root.left.left = tree_operations.TreeNode(4)
        root.left.right = tree_operations.TreeNode(5)
        root.right.left = tree_operations.TreeNode(6)
        root.right.right = tree_operations.TreeNode(7)

        # Calculate the height of the tree
        height = tree_operations.get_tree_height(root)

        # Check if the height is correct
        assert height == 2

    def test_get_tree_height_complex_tree_2(self):
        """
        Test the get_tree_height function with a more complex binary tree
        """
        # Create a complex binary tree
        root = tree_operations.TreeNode(1)
        root.left = tree_operations.TreeNode(2)
        root.right = tree_operations.TreeNode(3)
        root.left.left = tree_operations.TreeNode(4)
        root.left.right = tree_operations.TreeNode(5)
        root.right.left = tree_operations.TreeNode(6)
        root.right.right = tree_operations.TreeNode(7)
        root.left.left.left = tree_operations.TreeNode(8)
        root.left.left.left.left = tree_operations.TreeNode(9)
        root.left.left.left.left.right = tree_operations.TreeNode(10)

        # Calculate the height of the tree
        height = tree_operations.get_tree_height(root)

        # Check if the height is correct
        assert height == 5


# test serialize_tree
class TestSerializeTree:
    """
    Test the serialize_tree function
    """

    def test_serialize_tree_classic_small_tree(self):
        """
        Test the serialize_tree function with a classic small binary tree
        """
        # Create a simple binary tree
        root = tree_operations.TreeNode(1)
        root.left = tree_operations.TreeNode(2)
        root.right = tree_operations.TreeNode(3)

        # Serialize the tree
        serialized_tree = tree_operations.serialize_tree(root)

        # Check if the serialized tree is correct
        assert serialized_tree == [[1], [2, 3]]

    def test_serialize_tree_empty_tree(self):
        """
        Test the serialize_tree function with an empty binary tree
        """
        # Create an empty binary tree
        root = None

        # Serialize the tree
        serialized_tree = tree_operations.serialize_tree(root)

        # Check if the serialized tree is correct
        assert not serialized_tree

    def test_serialize_tree_single_node_tree(self):
        """
        Test the serialize_tree function with a single node binary tree
        """
        # Create a single node binary tree
        root = tree_operations.TreeNode(1)

        # Serialize the tree
        serialized_tree = tree_operations.serialize_tree(root)

        # Check if the serialized tree is correct
        assert serialized_tree == [[1]]

    def test_serialize_tree_complex_tree_1(self):
        """
        Test the serialize_tree function with a complex binary tree
        """
        # Create a complex binary tree
        root = tree_operations.TreeNode(1)
        root.left = tree_operations.TreeNode(2)
        root.right = tree_operations.TreeNode(3)
        root.left.left = tree_operations.TreeNode(4)
        root.left.right = tree_operations.TreeNode(5)
        root.right.left = tree_operations.TreeNode(6)
        root.right.right = tree_operations.TreeNode(7)

        # Serialize the tree
        serialized_tree = tree_operations.serialize_tree(root)

        # Check if the serialized tree is correct
        assert serialized_tree == [[1], [2, 3], [4, 5], [6, 7]]

    def test_serialize_tree_complex_tree_2(self):
        """
        Test the serialize_tree function with a more complex binary tree
        """
        # Create a complex binary tree
        root = tree_operations.TreeNode(1)
        root.left = tree_operations.TreeNode(2)
        root.right = tree_operations.TreeNode(3)
        root.left.left = tree_operations.TreeNode(4)
        root.left.right = tree_operations.TreeNode(5)
        root.right.left = tree_operations.TreeNode(6)
        root.right.right = tree_operations.TreeNode(7)
        root.left.left.left = tree_operations.TreeNode(8)
        root.left.left.left.left = tree_operations.TreeNode(9)
        root.left.left.left.left.right = tree_operations.TreeNode(10)

        # Serialize the tree
        serialized_tree = tree_operations.serialize_tree(root)

        # Check if the serialized tree is correct
        assert serialized_tree == [
            [1],
            [2, 3],
            [4, 5], [6, 7],
            [8, None], [None, None], [None, None], [None, None],
            [9, None],
            [None, 10]
        ]


# test deserialize_tree
class TestDeserializeTree:
    """
    Test the deserialize_tree function
    """

    def test_deserialize_tree_classic_small_tree(self):
        """
        Test the deserialize_tree function with a classic small binary tree
        """
        # Create a simple binary tree
        root = tree_operations.TreeNode(1)
        root.left = tree_operations.TreeNode(2)
        root.right = tree_operations.TreeNode(3)

        # Serialize the tree
        serialized_tree = tree_operations.serialize_tree(root)

        # Deserialize the tree
        deserialized_tree = tree_operations.deserialize_tree(serialized_tree)

        # Check if the deserialized tree is correct
        assert deserialized_tree.value == 1
        assert deserialized_tree.left.value == 2
        assert deserialized_tree.right.value == 3

    def test_deserialize_tree_empty_tree(self):
        """
        Test the deserialize_tree function with an empty binary tree
        """
        # Create an empty binary tree
        serialized_tree = []

        # Deserialize the tree
        deserialized_tree = tree_operations.deserialize_tree(serialized_tree)

        # Check if the deserialized tree is correct
        assert deserialized_tree is None

    def test_deserialize_tree_single_node_tree(self):
        """
        Test the deserialize_tree function with a single node binary tree
        """
        # Create a single node binary tree
        serialized_tree = [[1]]

        # Deserialize the tree
        deserialized_tree = tree_operations.deserialize_tree(serialized_tree)

        # Check if the deserialized tree is correct
        assert deserialized_tree.value == 1
        assert deserialized_tree.left is None
        assert deserialized_tree.right is None

    def test_deserialize_tree_complex_tree_1(self):
        """
        Test the deserialize_tree function with a complex binary tree
        """
        serialized_tree = [[1], [2, 3], [4, 5], [6, 7]]

        # Deserialize the tree
        deserialized_tree = tree_operations.deserialize_tree(serialized_tree)

        # Check if the deserialized tree is correct
        assert deserialized_tree.value == 1
        assert deserialized_tree.left.value == 2
        assert deserialized_tree.right.value == 3
        assert deserialized_tree.left.left.value == 4
        assert deserialized_tree.left.right.value == 5
        assert deserialized_tree.right.left.value == 6
        assert deserialized_tree.right.right.value == 7

    def test_deserialize_tree_complex_tree_2(self):
        """
        Test the deserialize_tree function with a more complex binary tree
        """
        # Create a complex binary tree
        serialized_tree = [
            [1],
            [2, 3],
            [4, 5], [6, 7],
            [8, None], [None, None], [None, None], [None, None],
            [9, None],
            [None, 10]
        ]

        # Deserialize the tree
        deserialized_tree = tree_operations.deserialize_tree(serialized_tree)

        # Check if the deserialized tree is correct
        assert deserialized_tree.value == 1
        assert deserialized_tree.left.value == 2
        assert deserialized_tree.right.value == 3
        assert deserialized_tree.left.left.value == 4
        assert deserialized_tree.left.right.value == 5
        assert deserialized_tree.right.left.value == 6
        assert deserialized_tree.right.right.value == 7
        assert deserialized_tree.left.left.left.value == 8
        assert deserialized_tree.left.left.left.left.value == 9
        assert deserialized_tree.left.left.left.left.right.value == 10
