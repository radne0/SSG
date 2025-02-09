from textnode import TextType,TextNode
from leafnode import LeafNode
import re


def extract_markdown_images(text):
       search_str = r"!\[(.*?)\]\((.*?)\)"
       matches = re.findall(search_str,text)
       return matches

def extract_markdown_links(text):
       search_str = r"(?<!!)\[(.*?)\]\((.*?)\)"
       matches = re.findall(search_str,text)
       return matches

def split_nodes_delimiter(oldnodes,delimiter,text_type):
        nodelist = []

        for n in oldnodes:
                if n.text_type != TextType.TEXT: 
                        nodelist.append(n)
                
                else:
                        text_nodes = n.text.split(delimiter)
                        if not(len(text_nodes) % 2):
                                raise Exception("delimiter mismatch")
                        for i,text in enumerate(text_nodes):
                                if (i%2):
                                        nodelist.append( TextNode(text,text_type))  
                                else:
                                        nodelist.append( TextNode(text,TextType.TEXT))
        return nodelist


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
                
    