import node_utils as nu
from textnode import TextType,TextNode


def test_extract_links():
    # Test 1: Basic single link
    text1 = "Here's a [simple link](https://example.com)"
    print("hello")
    print(nu.extract_markdown_links(text1))
    assert nu.extract_markdown_links(text1) == [("simple link", "https://example.com")]

    
    # Test 2: Multiple links
    text2 = "[link1](url1) and [link2](url2)"
    print(nu.extract_markdown_links(text2))    
    assert nu.extract_markdown_links(text2) == [("link1", "url1"), ("link2", "url2")]
    
    # Test 3: No links
    text3 = "Plain text without links"
    print(nu.extract_markdown_links(text3))    
    assert nu.extract_markdown_links(text3) == []

def test_extract_images():
    # Test 1: Basic single image
    text1 = "Here's an ![alt text](image.jpg)"
    print(nu.extract_markdown_images(text1))        
    assert nu.extract_markdown_images(text1) == [("alt text", "image.jpg")]
    
    # Test 2: Multiple images
    text2 = "![img1](url1.jpg) and ![img2](url2.jpg)"
    print(nu.extract_markdown_images(text2))    
    assert nu.extract_markdown_images(text2) == [("img1", "url1.jpg"), ("img2", "url2.jpg")]
    
    # Test 3: No images
    text3 = "Plain text without images"
    print(nu.extract_markdown_images(text3))    
    assert nu.extract_markdown_images(text3) == []

def main():
    test_extract_links()
    test_extract_images()

main()



