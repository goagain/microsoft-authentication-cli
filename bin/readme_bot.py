import re

pattern = re.compile(r"AZUREAUTH_VERSION = '(.+)'")

def extract_version_from_readme(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        return re.search(pattern, content).group(1)
    
def replace_versions(path: str, old_version:str, new_version:str):
    with open(path, 'r+', encoding='utf-8') as f:
        content = f.read()
        content = content.replace(old_version, new_version)

        f.seek(0)
        f.truncate()
        f.write(content)

def main():
    new_version = input("input a new SEMI_VERSION")
    old_version = extract_version_from_readme("./README.md")
    replace_versions("./README.md", old_version, new_version)