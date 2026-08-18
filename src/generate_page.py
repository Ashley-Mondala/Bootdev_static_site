import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        md = f.read()
    
    with open(template_path) as t:
        template = t.read()
    
    md_node = markdown_to_html_node(md)
    html_string = md_node.to_html()

    title = extract_title(md)
    

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    dest_path_dirname = os.path.dirname(dest_path)
    os.makedirs(dest_path_dirname, exist_ok=True)
    
    with open(dest_path, "w") as d:
        d.write(template)