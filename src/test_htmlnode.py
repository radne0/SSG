import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode

'''
class HTMLNode:

    def __init__(self,tag=None,value=None,children=None,props=None):

    def props_to_html(self):
        s=""
        for k in self.props:
            s+=f" {k}={self.props[k]}"

'''

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node =  HTMLNode("A",12,None,{"href":"http://www.google.com" ,  "target":"self"})
        print(node)
        print(node.props_to_html())

