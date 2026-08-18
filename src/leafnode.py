from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError()
        if not self.tag:
            return self.value
        
        result = f'<{self.tag}'
        if self.props:
            result += self.props_to_html()
        
        result += f'>{self.value}</{self.tag}>'
        
        return result
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
