import os
import re

def replace_in_string(text):
    text = re.sub(r'SecureCheck', 'SimSecure', text)
    text = re.sub(r'securecheck', 'simsecure', text)
    text = re.sub(r'Securecheck', 'Simsecure', text)
    text = re.sub(r'SECURECHECK', 'SIMSECURE', text)
    return text

def process_directory(root_dir):
    # 1. Replace content in files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            dirnames.remove('.git')
        
        for filename in filenames:
            if filename == 'rename_tool.py':
                continue
            
            filepath = os.path.join(dirpath, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = replace_in_string(content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated content in: {filepath}")
            except Exception as e:
                # ignore read errors for binaries
                pass

    # 2. Rename files and directories (bottom-up to avoid path invalidation)
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Rename files
        for filename in filenames:
            if filename == 'rename_tool.py':
                continue
            new_filename = replace_in_string(filename)
            if new_filename != filename:
                old_filepath = os.path.join(dirpath, filename)
                new_filepath = os.path.join(dirpath, new_filename)
                try:
                    os.replace(old_filepath, new_filepath)
                    print(f"Renamed file: {old_filepath} -> {new_filename}")
                except Exception as e:
                    print(f"Failed to rename file {old_filepath}: {e}")
        
        # Rename directories
        for dirname in dirnames:
            new_dirname = replace_in_string(dirname)
            if new_dirname != dirname:
                old_dirpath = os.path.join(dirpath, dirname)
                new_dirpath = os.path.join(dirpath, new_dirname)
                try:
                    os.replace(old_dirpath, new_dirpath)
                    print(f"Renamed directory: {old_dirpath} -> {new_dirname}")
                except Exception as e:
                    print(f"Failed to rename directory {old_dirpath}: {e}")

if __name__ == '__main__':
    process_directory(r'c:\Programming\RTRP')
