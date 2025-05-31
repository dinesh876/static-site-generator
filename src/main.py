from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.LINK:
            return LeafNode("a",text_node.text,f'{{href: "{text_node.url}"}}')
        case TextType.IMAGE:
            return LeafNode("i","",f'{{src:"{text_node.url}" alt: "{text_node.text}" }}')
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case _:
            print("Invalid text type")
    
    
def main():
    tn = TextNode("This is anchor text",TextType.BOLD,"https://example.com")
    text_node_to_html_node(tn)
    print(tn)
    
    hn = HTMLNode(props={"href":"http://example.com","target":"_blank"})
    print(hn.props_to_html())
    print(hn)
    
    leaf_node = LeafNode("p","hello world")
    print(leaf_node.to_html())
    
    leaf_node_1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node_1.to_html())
    
    
    parent_node = ParentNode(
        "p",
       [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(parent_node.to_html())

    

if __name__ == "__main__":
    main()