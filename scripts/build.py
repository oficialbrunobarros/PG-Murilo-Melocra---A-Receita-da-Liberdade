import os
import re

# Base paths
src_dir = 'src'
dist_dir = '.'
components_dir = 'componentes'

def load_component(name):
    path = os.path.join(components_dir, f"{name}.html")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    print(f"Warning: Component {name} not found!")
    return ""

def adjust_paths(content, depth):
    if depth == 0:
        return content
    
    # Calculate prefix, e.g., "../"
    prefix = "../" * depth
    
    # Replace static assets
    content = content.replace('src="static/', f'src="{prefix}static/')
    content = content.replace('href="static/', f'href="{prefix}static/')
    content = content.replace('`static/', f'`{prefix}static/')
    content = content.replace('"static/images/', f'"{prefix}static/images/')
    
    # Replace links
    content = content.replace('href="index.html', f'href="{prefix}index.html')
    content = content.replace('href="quem-somos.html', f'href="{prefix}quem-somos.html')
    content = content.replace('href="autores.html', f'href="{prefix}autores.html')
    content = content.replace('href="livros.html', f'href="{prefix}livros.html')
    content = content.replace('href="trilhas.html', f'href="{prefix}trilhas.html')
    content = content.replace('href="galeria.html', f'href="{prefix}galeria.html')
    content = content.replace('href="contato.html', f'href="{prefix}contato.html')
    content = content.replace('href="faq.html', f'href="{prefix}faq.html')
    content = content.replace('href="mapa-do-site.html', f'href="{prefix}mapa-do-site.html')
    content = content.replace('href="autoridade-editorial.html', f'href="{prefix}autoridade-editorial.html')
    content = content.replace('href="privacidade.html', f'href="{prefix}privacidade.html')
    content = content.replace('href="termos.html', f'href="{prefix}termos.html')
    
    # Replace action href inside navbar if it has specific page anchors
    # e.g., href="#navbar" inside subdirectory should not change unless they are absolute.
    return content

def compile_file(src_path, dest_path, depth):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace navbar and footer comments
    navbar_content = load_component("navbar")
    footer_content = load_component("footer")
    
    # Adjust paths inside navbar and footer based on depth before injecting them
    navbar_content = adjust_paths(navbar_content, depth)
    footer_content = adjust_paths(footer_content, depth)
    
    # Replace comments
    content = content.replace('<!-- INCLUDE_NAVBAR -->', navbar_content)
    content = content.replace('<!-- INCLUDE_FOOTER -->', footer_content)
    
    # Adjust remaining paths in the main page content
    content = adjust_paths(content, depth)
    
    # Ensure destination directory exists
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path:
        os.makedirs(dest_dir_path, exist_ok=True)
        
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Compiled: {src_path} -> {dest_path}")

def build():
    if not os.path.exists(src_dir):
        print(f"Error: {src_dir} directory does not exist! Please create it and add your source pages.")
        return
        
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.html'):
                src_path = os.path.join(root, file)
                
                # Compute relative path from src_dir
                rel_path = os.path.relpath(src_path, src_dir)
                dest_path = os.path.join(dist_dir, rel_path)
                
                # Determine subdirectory depth
                # e.g., "autores/murilo.html" -> depth 1
                # "index.html" -> depth 0
                parts = rel_path.split(os.sep)
                depth = len(parts) - 1
                
                compile_file(src_path, dest_path, depth)

if __name__ == "__main__":
    build()
