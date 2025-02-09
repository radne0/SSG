import node_utils as nu
from textnode import TextType,TextNode

def main():
    node = TextNode("Here is some text. `code here` **bold text** and some *italic text*",TextType.TEXT)
    out= nu.split_nodes_delimiter([node],"**",TextType.BOLD)
    out= nu.split_nodes_delimiter(out,"*",TextType.ITALIC)        
    out= nu.split_nodes_delimiter(out,"`",TextType.CODE)
    print(out)



main()



