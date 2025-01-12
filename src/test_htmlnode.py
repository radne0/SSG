import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_eq_url(self):
        node =  HTMLNode("A",12,None,{"href":"http://www.google.com" ,  "target":"self"})
        self.assertEqual(node.props_to_html(),' href="http://www.google.com" target="self"')

    def test_htmlnode_eq_no_url(self):
        node =  HTMLNode("P",12,None,{"style":"text-align:right"})
        self.assertEqual(node.props_to_html(),' style="text-align:right"')

    def test_htmlnode_const(self):
        node =  HTMLNode("A",12,None,{"href":"http://www.google.com" ,  "target":"self"})
        self.assertEqual(node.tag,"A")
        self.assertEqual(node.value,12)      
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,{"href": "http://www.google.com","target": "self"}    )            

    def test_htmlnode_tohtml(self):
        node =  HTMLNode("A",12,None,{"href":"http://www.google.com" ,  "target":"self"})
        with self.assertRaises(NotImplementedError):
            node.to_html()