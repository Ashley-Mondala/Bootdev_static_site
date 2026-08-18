import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):

    def test_all_texttype(self):
        result = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result
            )  
    
    def test_only_text(self):
        result = text_to_textnodes("Hi just Text")
        self.assertListEqual([TextNode("Hi just Text", TextType.TEXT)], result)

    def test_just_bold(self):
        result = text_to_textnodes("Hi **this is bold**")
        self.assertListEqual([TextNode("Hi ", TextType.TEXT), TextNode("this is bold", TextType.BOLD)], result)
    

if __name__ == "__main__":
    unittest.main()