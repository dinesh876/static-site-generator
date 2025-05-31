import unittest

from textnode import TextNode,TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)
    
    def test_neq(self):
        node = TextNode("This is a anchor node", TextType.LINK,"http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)
    
    def test_repr(self):
        node = TextNode("This is a anchor node", TextType.LINK.value,"http://example.com")
        self.assertEqual(str(node),"TextNode(This is a anchor node, link, http://example.com)")
        

if __name__ == "__main__":
    unittest.main()