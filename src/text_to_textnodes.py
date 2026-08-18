from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image_link import split_nodes_image, split_nodes_link

def text_to_textnodes(text) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    bold_textNodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    italics_textNodes = split_nodes_delimiter(bold_textNodes, "_", TextType.ITALIC)
    code_textNodes = split_nodes_delimiter(italics_textNodes, "`", TextType.CODE)
    images_textNodes = split_nodes_image(code_textNodes)
    result = split_nodes_link(images_textNodes)

    return result
