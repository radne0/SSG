import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node =  TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node =  TextNode("TestNode",TextType.BOLD,"http://www.google.com")  
        node2 = TextNode("TestNode",TextType.BOLD,"http://www.google.com")
        self.assertEqual(node,node2)

    def test_noteq_text(self):
        node =  TextNode("TestNode 2",TextType.NORMAL,"http://www.google.com")  
        node2 = TextNode("TestNode",TextType.NORMAL,"http://www.google.com")
        self.assertNotEqual(node,node2)

    def test_noteq_type(self):
        node =  TextNode("TestNode",TextType.NORMAL,"http://www.google.com")  
        node2 = TextNode("TestNode",TextType.ITALIC,"http://www.google.com")
        self.assertNotEqual(node,node2)

    def test_noteq_url(self):
        node =  TextNode("TestNode",TextType.BOLD,"http://www.google.com")  
        node2 = TextNode("TestNode",TextType.BOLD,"http://www.yahoo.com")
        self.assertNotEqual(node,node2)

    def test_noteq_url2(self):
        node =  TextNode("TestNode",TextType.BOLD)  
        node2 = TextNode("TestNode",TextType.BOLD,"http://www.yahoo.com")
        self.assertNotEqual(node,node2)



if __name__ == "__main__":
    unittest.main()
