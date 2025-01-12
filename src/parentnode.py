from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if (self.tag == None): 
            raise ValueError("Tag missing...")
        s = f"<{self.tag}{self.props_to_html()}>"    
        for c in self.children:
            s+= c.to_html()
        s+=f"</{self.tag}>"
        return s

