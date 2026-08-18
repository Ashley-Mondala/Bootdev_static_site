def markdown_to_blocks(markdown) -> list[str]:
    result = list()
    if not markdown:
        return result

    modified_markdown = markdown.split("\n\n")

    for block in modified_markdown:
        
        modified_block = block.split("\n")
        fixed_block = list()
        for line in modified_block:
            temp = line.strip()
            if not temp:
                continue
            fixed_block.append(temp)
        if not fixed_block:
            continue
        result.append("\n".join(fixed_block))
    
    return result