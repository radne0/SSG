import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
import node_utils as nu

class TestNodeUtils(unittest.TestCase):

    def test_util_link(self):

        text1 = "Here's a [simple link](https://example.com)"
        self.assertEqual(nu.extract_markdown_links(text1),[("simple link", "https://example.com")])

    def test_util_link_double(self):
        text2 = "[link1](url1) and [link2](url2)"  
        self.assertEqual(nu.extract_markdown_links(text2), [("link1", "url1"), ("link2", "url2")])

    def test_util_link_empty(self):
        text3 = "Plain text without links" 
        self.assertEqual(nu.extract_markdown_links(text3), [])



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


    def test_util_splittext_simple_bold(self):
        node = TextNode("Hello **this text is bold** stuff",TextType.TEXT)
        out= nu.split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual( len(out),3)
        self.assertEqual( out[0].text_type, TextType.TEXT)
        self.assertEqual( out[1].text_type, TextType.BOLD)        
        self.assertEqual( out[2].text_type, TextType.TEXT)
        self.assertEqual( out[0].text,"Hello "   )   
        self.assertEqual( out[1].text,"this text is bold"   )   
        self.assertEqual( out[2].text," stuff"   )   

    def test_util_splittext_bold_start(self):
        node = TextNode("**this text is bold** stuff",TextType.TEXT)
        out= nu.split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual( len(out),3)
        self.assertEqual( out[0].text_type, TextType.TEXT)
        self.assertEqual( out[1].text_type, TextType.BOLD)
        self.assertEqual( out[2].text_type, TextType.TEXT)
        self.assertEqual( out[0].text,""   )   
        self.assertEqual( out[1].text,"this text is bold"   )   
        self.assertEqual( out[2].text," stuff"   )   

    def test_util_splittext_bold_end(self):
        node = TextNode("Here is some text **this text is bold**",TextType.TEXT)
        out= nu.split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual( len(out),3)
        self.assertEqual( out[0].text_type, TextType.TEXT)
        self.assertEqual( out[1].text_type, TextType.BOLD)
        self.assertEqual( out[2].text_type, TextType.TEXT)
        self.assertEqual( out[0].text,"Here is some text "   )   
        self.assertEqual( out[1].text,"this text is bold"   )   
        self.assertEqual( out[2].text,""   )   

    def test_util_splittext_bold_and_code(self):
        node = TextNode("Here is some text. `code here` **bold text** and regular text",TextType.TEXT)
        out= nu.split_nodes_delimiter([node],"**",TextType.BOLD)
        out= nu.split_nodes_delimiter(out,"`",TextType.CODE)

        self.assertEqual( len(out),5)
        self.assertEqual(out[0].text_type, TextType.TEXT)  
        self.assertEqual(out[1].text_type, TextType.CODE)  
        self.assertEqual(out[2].text_type, TextType.TEXT)  
        self.assertEqual(out[3].text_type, TextType.BOLD)  
        self.assertEqual(out[4].text_type, TextType.TEXT)    
        self.assertEqual(out[0].text, "Here is some text. ")  
        self.assertEqual(out[1].text, "code here")  
        self.assertEqual(out[2].text, " ")  
        self.assertEqual(out[3].text, "bold text")  
        self.assertEqual(out[4].text, " and regular text")          

    def test_util_splittext_bold_and_code_italic(self):
        node = TextNode("Here is some text. `code here` **bold text** and some *italic text*",TextType.TEXT)
        out= nu.split_nodes_delimiter([node],"**",TextType.BOLD)
        out= nu.split_nodes_delimiter(out,"*",TextType.ITALIC)        
        out= nu.split_nodes_delimiter(out,"`",TextType.CODE)

        self.assertEqual( len(out),7)
        self.assertEqual(out[0].text_type, TextType.TEXT)  
        self.assertEqual(out[1].text_type, TextType.CODE)  
        self.assertEqual(out[2].text_type, TextType.TEXT)  
        self.assertEqual(out[3].text_type, TextType.BOLD)  
        self.assertEqual(out[4].text_type, TextType.TEXT)    
        self.assertEqual(out[5].text_type, TextType.ITALIC)  
        self.assertEqual(out[6].text_type, TextType.TEXT)            
        self.assertEqual(out[0].text, "Here is some text. ")  
        self.assertEqual(out[1].text, "code here")  
        self.assertEqual(out[2].text, " ")  
        self.assertEqual(out[3].text, "bold text")  
        self.assertEqual(out[4].text, " and some ")        
        self.assertEqual(out[5].text, "italic text")    
        self.assertEqual(out[6].text, "")      
 

 