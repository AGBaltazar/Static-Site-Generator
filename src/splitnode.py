from textnode import *
from htmlnode import *

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