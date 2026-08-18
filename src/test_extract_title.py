import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_with_h1(self):
        md = """
                # Hello
            """
        
        self.assertEqual(extract_title(md), "Hello")
    
    def test_no_h1(self):
        md = """
            ## Fail
        """
        with self.assertRaises(Exception):
            extract_title(md)