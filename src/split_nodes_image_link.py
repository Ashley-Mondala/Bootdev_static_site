from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes = list()

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            split_nodes.append(old_node)
            continue

        extracted_node = extract_markdown_images(old_node.text)
        remaining_text = old_node.text

        for node in extracted_node:
            rebuilt_markdown = f"![{node[0]}]({node[1]})"
            sections = remaining_text.split(rebuilt_markdown)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(node[0], TextType.IMAGE, node[1]))
            remaining_text = sections[-1]

        if remaining_text:
            split_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return split_nodes
        


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes = list()

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            split_nodes.append(old_node)
            continue

        extracted_node = extract_markdown_links(old_node.text)
        remaining_text = old_node.text

        for node in extracted_node:
            rebuilt_markdown = f"[{node[0]}]({node[1]})"
            sections = remaining_text.split(rebuilt_markdown)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(node[0], TextType.LINK, node[1]))
            remaining_text = sections[-1]

        if remaining_text:
            split_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return split_nodes