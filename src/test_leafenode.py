import unittest


from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):

        #basic node
        leaf1 = LeafNode("p", "This is a paragraph of text.")

        #node with properties...
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leaf3 = LeafNode("a", "Click!", {"href":"https://www.google.com", "target":"_blank"   }    )

        leaf4 = LeafNode(None,"hmmm")

        print(leaf1.to_html())
        print(leaf2.to_html())
        print(leaf3.to_html())
        print(leaf4.to_html())