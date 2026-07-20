import re

def check_html_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean up comments
    html_clean = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    
    # Clean up tags that do not have closing tags in HTML5
    void_tags = ['meta', 'link', 'img', 'br', 'hr', 'input']
    for vt in void_tags:
        html_clean = re.sub(rf'<{vt}\b[^>]*>', '', html_clean, flags=re.IGNORECASE)

    # Find all tags
    tags = re.findall(r'</?([a-zA-Z0-9:-]+)\b[^>]*>', html_clean)
    
    stack = []
    errors = []
    
    # We will trace divs specifically
    div_count = 0
    
    for i, tag in enumerate(re.finditer(r'(</?([a-zA-Z0-9:-]+)\b[^>]*>)', html_clean)):
        tag_str, tag_name = tag.groups()
        tag_name = tag_name.lower()
        
        if tag_str.startswith('</'):
            if not stack:
                errors.append(f"Extra closing tag {tag_str} at position {tag.start()}")
            else:
                last_open = stack.pop()
                if last_open != tag_name:
                    errors.append(f"Mismatched closing tag {tag_str} for opening tag <{last_open}>")
        else:
            stack.append(tag_name)
            
    print(f"File checked: {filepath}")
    print(f"Stack size at end (should be 0 if balanced): {len(stack)}")
    if stack:
        print(f"Unclosed tags remaining on stack: {stack}")
    if errors:
        print(f"Errors found: {errors}")
    else:
        print("No structural tag errors found.")

if __name__ == "__main__":
    check_html_tags("src/quem-somos.html")
