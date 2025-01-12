import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
import node_utils as nu

class TestNodeUtils(unittest.TestCase):
    def test_util_text(self):
        node = TextNode("Some Text",TextType.TEXT) 
        new_node = nu.text_node_to_html_node(node)
        self.assertEqual(new_node.to_html(), "Some Text")

    def test_util_bold(self):
        node = TextNode("Some Bold Text",TextType.BOLD) 
        new_node = nu.text_node_to_html_node(node)
        self.assertEqual(new_node.to_html(), "<b>Some Bold Text</b>")

    def test_util_italic(self):
        node = TextNode("Some Italic Text",TextType.ITALIC) 
        new_node = nu.text_node_to_html_node(node)
        self.assertEqual(new_node.to_html(), "<i>Some Italic Text</i>")

    def test_util_code(self):
        node = TextNode("Some Code Text!",TextType.CODE) 
        new_node = nu.text_node_to_html_node(node)
        self.assertEqual(new_node.to_html(), "<code>Some Code Text!</code>")

    def test_util_link(self):
        node = TextNode("Click me!",TextType.LINK,"http://www.google.com") 
        new_node = nu.text_node_to_html_node(node)
        self.assertEqual(new_node.to_html(), "<a href=\"http://www.google.com\">Click me!</a>")

    def test_util_image(self):
        node = TextNode("Some alt text",TextType.IMAGE,"images/menu.jpg") 
        new_node = nu.text_node_to_html_node(node)
        self.assertEqual(new_node.to_html(), "<img src=\"images/menu.jpg\" alt=\"Some alt text\"></img>")

    def test_util_invalid(self):
        node = TextNode("some text","bool")
        with self.assertRaises(ValueError):
            new_node = nu.text_node_to_html_node(node)


    def test_util_link_no_url(self):
        node = TextNode("",TextType.LINK,None) 
        with self.assertRaises(ValueError):
            new_node = nu.text_node_to_html_node(node)

    def test_util_img_no_src(self):
        node = TextNode("",TextType.IMAGE,None) 
        with self.assertRaises(ValueError):
            new_node = nu.text_node_to_html_node(node)

