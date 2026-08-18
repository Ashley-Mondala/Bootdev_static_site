from markdown_to_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from htmlnode import HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from parentnode import ParentNode
from leafnode import LeafNode

def text_to_children(block):
    leafnode_list = list()
    child_node = text_to_textnodes(block)
    for node in child_node:
        leafnode_list.append(text_node_to_html_node(node))
    
    return leafnode_list

def paragraph_to_html_node(block) -> ParentNode:
    split_block = block.split("\n")
    child = text_to_children(" ".join(split_block))
    return ParentNode(tag="p", children=child)

def heading_to_html_node(block) -> ParentNode:
    count = 0
    for i in range(6):
        if block[i] == " ":
            break
        count += 1
    child = text_to_children(block[count + 1:])
    return ParentNode(tag=f"h{count}", children=child)

def code_to_html_node(block) -> ParentNode:
    block_stripped = block.removeprefix("```\n")
    block_stripped = block_stripped.removesuffix("```")
    node = TextNode(text=block_stripped, text_type=TextType.CODE)
    return ParentNode(tag="pre", children=[text_node_to_html_node(node)])

def quote_to_html_node(block) -> ParentNode:
    split_blocks = block.split("\n")
    to_rejoin = list()
    for line in split_blocks:
        temp = line.removeprefix(">")
        temp = temp.strip()
        to_rejoin.append(temp)
    
    child = text_to_children("\n".join(to_rejoin))
    return ParentNode(tag="blockquote", children=child)

def unordered_list_to_html_node(block) -> ParentNode:
    split_blocks = block.split("\n")
    unordered_parent = list()
    for line in split_blocks:
        temp = line.removeprefix("- ")
        child = text_to_children(temp)
        unordered_parent.append(ParentNode(tag="li", children=child))
    
    return ParentNode(tag="ul", children = unordered_parent)

def ordered_list_to_html_node(block):
    split_block = block.split("\n")
    ordered_parent = list()
    for line in split_block:
        temp = line.split(". ")[1]
        child = text_to_children(temp)
        ordered_parent.append(ParentNode(tag="li", children=child))
    
    return ParentNode(tag="ol", children=ordered_parent)



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child = list()
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            child.append(paragraph_to_html_node(block))
        
        elif block_type == BlockType.HEADING:
            child.append(heading_to_html_node(block))
        
        elif block_type == BlockType.CODE:
            child.append(code_to_html_node(block))
        
        elif block_type == BlockType.QUOTE:
            child.append(quote_to_html_node(block))
        
        elif block_type == BlockType.UNORDERED_LIST:
            child.append(unordered_list_to_html_node(block))
        
        elif block_type == BlockType.ORDERED_LIST:
            child.append(ordered_list_to_html_node(block))
    
    return ParentNode(tag="div", children=child)
        