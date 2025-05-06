class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_list = []
        if self.props:
            for key, value in self.props.items():
                props_list.append(f' { key}="{value}"')
        return "".join(props_list)
    
    def __repr__(self):
        return (f"HTMLNode({self.tag} {self.value} {self.children} {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.value = value
        self.tag = tag

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return (f"{self.value}")
        else:
            return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
            

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children

    def to_html(self):
        if self.tag == None:
            raise ValueError
        elif self.children == None:
            raise ValueError("Whoops where are the Kids!")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

