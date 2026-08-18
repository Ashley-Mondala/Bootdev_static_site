import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node2.to_html(), "<p>This is a paragraph of text.</p>")
        
if __name__ == "__main__":
    unittest.main()