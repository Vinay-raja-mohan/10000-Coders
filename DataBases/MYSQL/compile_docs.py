import os
import re

base_dir = r"c:\Course\10000-Coders\DataBases\MYSQL"
output_file = r"C:\Users\Vinay\.gemini\antigravity\brain\e6fd3ae1-1245-42da-b548-ddd45041dc92\Course_Documentation.md"

# Get all Day folders
folders = []
for f in os.listdir(base_dir):
    full_path = os.path.join(base_dir, f)
    if os.path.isdir(full_path) and re.match(r'(?i)Day[-_]?\d+', f):
        num = int(re.search(r'\d+', f).group())
        folders.append((num, full_path, f))

# Sort by day number
folders.sort(key=lambda x: x[0])

with open(output_file, 'w', encoding='utf-8') as out:
    out.write("# MySQL Course Documentation (Day 1 to 21)\n\n")
    
    for num, path, folder_name in folders:
        if num > 21:
            continue
            
        out.write(f"## {folder_name.upper()}\n\n")
        
        # Get files inside the folder
        files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
        # Sort files to prioritize main day files
        files.sort(key=lambda x: (not x.lower().startswith('day'), x))
        
        for file in files:
            file_path = os.path.join(path, file)
            out.write(f"### {file}\n\n")
            
            ext = os.path.splitext(file)[1].lower()
            lang = "sql" if ext == ".sql" else "text"
            
            out.write(f"```{lang}\n")
            try:
                with open(file_path, 'r', encoding='utf-8') as f_in:
                    content = f_in.read()
                    out.write(content)
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as f_in:
                    content = f_in.read()
                    out.write(content)
            except Exception as e:
                out.write(f"Error reading file: {e}")
                
            out.write("\n```\n\n")

print(f"Documentation compiled successfully to {output_file}")
