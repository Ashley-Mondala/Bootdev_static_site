import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node2 = HTMLNode("<p>", "hi")
        node1 = HTMLNode("<a>", "mer", [node2], {"href": "https://www.google.com"})
    
        node3 = HTMLNode("<h1>", "why", props={"href": "https://www.google.com", "target": "_blank",})
        print(node1.props_to_html())
        print(node2.props_to_html())
        print(node3.props_to_html())

if __name__ == "__main__":
    unittest.main()