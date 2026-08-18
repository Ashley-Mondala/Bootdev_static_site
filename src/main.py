import os
import shutil
from textnode import TextNode, TextType
from generate_page import generate_page, generate_pages_recursive


def copy_static_content_to_public_dir(src, dir):
    src_items = os.listdir(src)
    
    for item in src_items:
        src_path = os.path.join(src, item) 
        if os.path.isdir(src_path):
            dir_path = os.path.join(dir, item)
            os.mkdir(dir_path)
            copy_static_content_to_public_dir(src_path, dir_path)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dir)

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    dir_path = "public"
    src_path = "static"
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)
    copy_static_content_to_public_dir(src_path,dir_path)

    generate_pages_recursive("content", "template.html", "public")
    
if __name__ == "__main__":
    main()