import unittest
from splitnode import *

class TestSplitNode(unittest.TestCase):
    def test_text(self):
        node = (TextNode("This is text with a `code block` word", TextType.TEXT))
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()