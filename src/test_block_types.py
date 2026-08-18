import unittest
from block_types import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):

    def test_header_type(self):
        block = block_to_block_type("## Heading")
        self.assertEqual(block, BlockType.HEADING)

    def test_code(self):
        block = block_to_block_type("```\ncode here```")
        self.assertEqual(block, BlockType.CODE)
    
    def test_quote(self):
        block = block_to_block_type("> this\n> is\n> a\n>quote")
        self.assertEqual(block, BlockType.QUOTE)
    
    def test_unordered_list(self):
        block = block_to_block_type("- list1\n- list2\n- list3")
        self.assertEqual(block, BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        block = block_to_block_type("1. list1\n2. list2\n3. list3")
        self.assertEqual(block, BlockType.ORDERED_LIST)
    
    def test_paragraph(self):
        block = block_to_block_type("hi")
        self.assertEqual(block, BlockType.PARAGRAPH)
    
    def test_faulty_ordered_list(self):
        block = block_to_block_type("1. list1\n4. list2\n3. list3")
        self.assertEqual(block, BlockType.PARAGRAPH)