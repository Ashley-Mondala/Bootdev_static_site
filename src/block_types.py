from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block) -> BlockType:
    
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        quote_split = block.split("\n")
        
        for line in quote_split:
            if not line.startswith(">"):
                break
        else:
            return BlockType.QUOTE
    
    if block.startswith("- "):
        unordered_list_split = block.split("\n")
        
        for line in unordered_list_split:
            if not line.startswith("- "):
                break
        else:
            return BlockType.UNORDERED_LIST
    
    if block.startswith("1. "):
        count = 1
        ordered_list_split = block.split("\n")
        
        for line in ordered_list_split:
            
            if not line.startswith(f"{count}. "):
                break

            count += 1
        
        else:
            return BlockType.ORDERED_LIST
    
    
    return BlockType.PARAGRAPH
