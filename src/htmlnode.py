class HTMLNode:
    
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise Exception("NotImplementedError")

    def props_to_html(self):
        props_to_html = ""
        for key in self.props:
            props_to_html += f'{key}={self.props[key]} '
        return props_to_html
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.tag},{self.value},{self.props},{self.children})'


class LeafNode(HTMLNode):
    
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag=tag,value=value,props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("leaf nodes must have a value")
        if not self.tag:
            return self.value
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        props = super().props_to_html()
        return f"<{self.tag} {props}>{self.value}</{self.tag}>"



class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be empty")
        
        if self.children is None:
            raise ValueError("Children cannot be empty")
        
        html = f"<{self.tag}>"
        for node in self.children:
            html += f"{node.to_html()}"
        html += f"</{self.tag}>"
        
        return html

    