from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "plain"    # Plain
    BOLD = "bold"      # **Bold text**
    ITALIC = "italic"  # _Italic text_
    CODE = "code"      # `Code text`
    LINK = "link"           # [anchor text](url)
    IMAGE = "image"         # ![alt text](url)

class TextNode:
    def __init__(self, text: str, text_type: TextType, url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode) -> bool:
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match (text_node.text_type):
        
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        
        case TextType.LINK:
            return LeafNode("a", text_node.text, {'href': text_node.url})
        
        case TextType.IMAGE:
            return LeafNode("img", "", {'src': text_node.url, 'alt': text_node.text})

        case _:
            raise Exception("Not valid text type")
