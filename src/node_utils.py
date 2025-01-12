from textnode import TextType,TextNode
from leafnode import LeafNode

def split_nodes_delimiter(oldnodes,delimiter,text_type):
        text = oldnodes.text.split(delimiter)
        print(text)




def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
                return LeafNode("b",text_node.text)
        case TextType.ITALIC:
                return LeafNode("i",text_node.text)
        case TextType.CODE:
                return LeafNode("code",text_node.text)
        case TextType.LINK:
                if (text_node.url == None): raise ValueError("TextNode -> LeafNode failed: no url to convert to a link")
                return LeafNode("a",text_node.text, { "href":f"{text_node.url}"   }     )
        case TextType.IMAGE:
                if (text_node.url == None): raise ValueError("TextNode -> LeafNode failed: no img src to convert to a link")
                return LeafNode("img","", { "src":f"{text_node.url}","alt":f"{text_node.text}"    }     )
        case _:
                raise ValueError("Unknown Type or type missing.")
                
    