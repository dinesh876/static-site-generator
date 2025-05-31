import unittest

from textnode import TextNode,TextType
from htmlnode import LeafNode,HTMLNode,ParentNode
from main import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p","This is a text node")
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),"<p>This is a text node</p>")
        self.assertEqual(node1.to_html(),"<a href=https://www.google.com >Click me!</a>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        

if __name__ == "__main__":
    unittest.main()