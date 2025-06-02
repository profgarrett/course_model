import os

root = 'chapters'  # Update this path

for dirpath, dirnames, filenames in os.walk(root):
    print(f"Processing directory: {dirpath}")
    md_files = [f for f in filenames if f.lower().endswith('.md')]
    print(f"Found markdown files: {md_files}")
    if len(md_files) == 1:
        old_path = os.path.join(dirpath, md_files[0])
        new_path = os.path.join(dirpath, 'index.md')
        print(f"Renaming {old_path} to {new_path}")
        if old_path != new_path:
            print(f"Renaming {old_path} -> {new_path}")
            os.rename(old_path, new_path)



for dirpath, dirnames, filenames in os.walk(root):
    print(f"Processing directory: {dirpath}")
    md_files = [f for f in filenames if f.lower().endswith('.ipynb')]
    print(f"Found markdown files: {md_files}")
    if len(md_files) == 1:
        old_path = os.path.join(dirpath, md_files[0])
        new_path = os.path.join(dirpath, 'index.ipynb')
        print(f"Renaming {old_path} to {new_path}")
        if old_path != new_path:
            print(f"Renaming {old_path} -> {new_path}")
            os.rename(old_path, new_path)