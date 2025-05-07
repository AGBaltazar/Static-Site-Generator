from textnode import *
from htmlnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != text_type.TEXT:
            result.append(node)
            continue
        text = node.text
        if delimiter not in text:
            result.append(node)
            continue
        split_node = text.split(delimiter)

        if len(split_node) % 2 ==0:
            raise Exception
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
                
            if i % 2 == 0:
                # Even index: regular text
                result.append(TextNode(split_node[i], TextType.TEXT))
            else:
                # Odd index: special type (code, bold, etc.)
                result.append(TextNode(split_node[i], text_type))
    return result

def extract_markdown_images(text):
    image_match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_match
        

def extract_markdown_links(text):
    link_match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_match

def split_nodes_image(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        images = extract_markdown_images(node.text)
                                         
        if not images:
            results.append(node)
            continue

        remaining_text = node.text
        
        for alt_text, image_url in images:
            image_markdown = f"![{alt_text}]({image_url})"
            parts = remaining_text.split(image_markdown, 1)
            
            if parts[0]:
                results.append(TextNode(parts[0], TextType.TEXT))
                
            results.append(TextNode(alt_text, TextType.IMAGE, image_url))
            
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
                
        if remaining_text:
            results.append(TextNode(remaining_text, TextType.TEXT))

def split_nodes_link(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        
        if not links:
            results.append(node)
            continue
            
        remaining_text = node.text
        
        for text, url in links:
            link_markdown = f"[{text}]({url})"
            parts = remaining_text.split(link_markdown, 1)
            
            if parts[0]:
                results.append(TextNode(parts[0], TextType.TEXT))
                
            results.append(TextNode(text, TextType.LINK, url))
            
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
                
        if remaining_text:
            results.append(TextNode(remaining_text, TextType.TEXT))
    
    return results

def text_to_textnodes(text):
    # Create initial TextNode with the raw text
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Process with delimiters
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Process images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes

def markdown_to_blocks(markdown):
    new_list = []
    split_text = markdown.split("\n\n")
    for text in split_text:
        stripped_text = text.strip()
        if stripped_text:
         new_list.append(stripped_text)
    return new_list

    