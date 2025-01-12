import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_eq_basic(self):

        node = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_eq_basic2(self):

        node = ParentNode(
            "table",
            [
                ParentNode("tr",
                [
                    LeafNode("td","Tim"), 
                    LeafNode("td","Jefferson"),
                    LeafNode("td","(302)-432-1030"),
                    LeafNode("td","122 Meadowbrook Lane"),
                    LeafNode("td","Springfield"),
                    LeafNode("td","Ohio")                 
                ]),
                ParentNode("tr",
                [
                    LeafNode("td","Jack"), 
                    LeafNode("td","Edwards"),
                    LeafNode("td","(302)-332-1213"),
                    LeafNode("td","122 Gooding Dr."),
                    LeafNode("td","Springfield"),
                    LeafNode("td","Ohio")                 
                ]),                       
            ]
        )
        self.maxDiff=None
        self.assertEqual(node.to_html(),'''<table><tr><td>Tim</td><td>Jefferson</td><td>(302)-432-1030</td><td>122 Meadowbrook Lane</td><td>Springfield</td><td>Ohio</td></tr><tr><td>Jack</td><td>Edwards</td><td>(302)-332-1213</td><td>122 Gooding Dr.</td><td>Springfield</td><td>Ohio</td></tr></table>''')
       
                                    
    def test_parent_eq_basic_props(self):
        node = ParentNode(
            "div",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal Text"),
            ],
            {"class":"main", "script":"test.js"}
        )        
        self.assertEqual(node.to_html(),'<div class="main" script="test.js"><b>Bold text</b>Normal Text</div>')


    def test_parentnode_deepnest(self):
        node = ParentNode("p", [ParentNode("div"
                                    ,[ParentNode("b",
                                        [ParentNode("i", 
                                            [LeafNode("a","click this")])])])])


                         
        self.assertEqual(node.to_html(),'<p><div><b><i><a>click this</a></i></b></div></p>')

    def test_parentnode_deepnest2(self):
        node = ParentNode("p",   
                           [ParentNode("div", [ 
                               ParentNode("a", [ LeafNode("p","Click this!")    ], {"href":"http://www.test.com"}        )   
                             ], {"id":"test"}   )      ])
        self.assertEqual(node.to_html(),'<p><div id="test"><a href="http://www.test.com"><p>Click this!</p></a></div></p>')

    def test_parentnode_no_tag(self):
        node = ParentNode(None,[])
        with self.assertRaises(ValueError):
            node.to_html()
