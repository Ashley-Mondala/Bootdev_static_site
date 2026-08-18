from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    
    nodes_list = list()

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes_list.append(old_node)
            continue

        blocks_of_texts = old_node.text.split(delimiter)

        if not len(blocks_of_texts) % 2:
            raise Exception("Invalid Markdown Syntax")
        
        new_created_text_node = list()
        
        for i in range(len(blocks_of_texts)):
            if not blocks_of_texts[i]:
                continue
                
            if i % 2 == 1:
                new_created_text_node.append(TextNode(blocks_of_texts[i], text_type))
            else:
                new_created_text_node.append(TextNode(blocks_of_texts[i], TextType.TEXT))
        
        nodes_list.extend(new_created_text_node)

    return nodes_list



            
        

