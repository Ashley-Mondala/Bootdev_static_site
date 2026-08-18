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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_list = os.listdir(dir_path_content)
    
    for entry in content_list:
        new_dir_path_content = os.path.join(dir_path_content, entry)
        new_dest_dir_path = os.path.join(dest_dir_path, entry)
        
        if os.path.isfile(new_dir_path_content):
            
            if not entry.endswith(".md"):
                continue

            generate_page(new_dir_path_content, template_path, new_dest_dir_path.replace(".md", ".html"))
        
        else:
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)