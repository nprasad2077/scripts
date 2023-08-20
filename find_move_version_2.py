from pathlib import Path

# Specify the paths
source_folder = Path('/mnt/e/property/')
target_folder = Path('/mnt/d/property_out/')

# Keyword to search for
keyword = input('partial file name: ').lower()

print(keyword)

# Walk through the source folder and its subdirectories
for file_path in source_folder.glob('**/*'):
    if keyword in file_path.name.lower():
        target_path = target_folder / file_path.relative_to(source_folder)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.rename(target_path)
        print(f"Moved {file_path.name} to {target_path}")
