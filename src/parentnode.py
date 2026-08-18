from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict = None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Missing Tag")
        if not self.children:
            raise ValueError("Has no child")
        
        result = f'<{self.tag}'
        if self.props:
            result += self.props_to_html()
        result += '>'
        for child in self.children:
            result += child.to_html()
        
        result += f"</{self.tag}>"
       
        return result

