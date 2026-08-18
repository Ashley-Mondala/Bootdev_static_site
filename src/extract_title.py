def extract_title(markdown) -> str:
    markdown_split = markdown.split("\n")
    for line in markdown_split:
        temp = line.strip()
        if temp.startswith("# "):
            return temp[2:]
    else:
        raise Exception("No h1 header in Markdown")