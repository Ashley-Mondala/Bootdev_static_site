import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_tag(self):
        child_node = ParentNode("span", "child")
        parent_node = ParentNode(None, [child_node])

        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_child(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_mixedchild(self):
        grandchild = LeafNode("d", "pog")
        child_node = ParentNode("b", [grandchild])
        child2_node = LeafNode("c", "bruh")
        parent_node = ParentNode("a", [child_node, child2_node])
        self.assertEqual(parent_node.to_html(), "<a><b><d>pog</d></b><c>bruh</c></a>")
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("a", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(parent_node.to_html(), '<a href="https://www.google.com"><span>child</span></a>')