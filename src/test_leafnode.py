import unittest


from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_eq(self):

        #basic node
        leaf1 = LeafNode("p", "This is a paragraph of text.")

        #node with properties...
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leaf3 = LeafNode("a", "Click!", {"href":"https://www.google.com", "target":"_blank"   }    )

        #no tag, plain text...
        leaf4 = LeafNode(None,"hmmm")

        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")  
        self.assertEqual(leaf3.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click!</a>")
        self.assertEqual(leaf4.to_html(),"hmmm")

