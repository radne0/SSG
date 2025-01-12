import node_utils as nu
from textnode import TextType,TextNode

def main():
    node = TextNode("This has a `code block` here!",TextType.TEXT)
    new_nodes = nu.split_nodes_delimiter(node,'`',TextType.CODE)
main()



