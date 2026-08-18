import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_codeblock_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ]                 
        )

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ]
        )

    def test_no_text_typetext(self):
        node = TextNode("This is text with a italic word", TextType.ITALIC)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), 
                        [TextNode("This is text with a italic word", TextType.ITALIC)])
    

    def test_multi_node_with_code_delimiter(self):
        node1 = TextNode("This is text with a italic word", TextType.ITALIC)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node1, node2], "`", TextType.CODE), 
            [
                TextNode("This is text with a italic word", TextType.ITALIC),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ]                 
        )

    def test_missing_end_markdown_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()