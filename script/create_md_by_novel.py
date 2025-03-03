import os


def create_md(path, title):
    res = os.system(f'hugo new content "{path}{title}.md" ')
    print(res, 1)
    file = f'{path}{title}.md'
    with open(file, encoding='UTF-8', mode='r') as f:
        lines:list[str] = f.readlines()            
        lines = map(lambda x: x.replace("draft: true", "draft: false"), lines)
        lines = map(lambda x: x.replace("tag:", "tag: 恶役千金的矜持"), lines)
        lines = map(lambda x: x.replace("categories:", "categories: 生活"), lines)

    with open(file, encoding='UTF-8', mode='w') as f:
        f.writelines(lines)

def modify_md(md_path, novel: list[str]):
    with open(md_path, encoding='UTF-8', mode='a') as f:
        novel[0] = "## " + novel[0]
        novel = map(lambda x: x + "\n", novel)
        f.writelines(novel)

def read_novel(novel_path) -> list[str]:
    with open(novel_path, encoding='utf-8', mode='r') as f:
        lines = f.readlines()
    return lines


def main():
    path = "./content/post/B-生活/恶役千金的矜持/"
    novel_dir = r"C:\code\application\crawler_for_novel\translated"
    files = os.listdir(novel_dir)
    files.sort(key=lambda x: int(x.split("_")[0]))
    for f in  files:
        name = f.split("_")
        num = int(name[0]) 
        title = name[1].split(".")[0]
        title = f"第{num}节_{title}"   
        create_md(path=path, title=title)
        novel = read_novel(f"{novel_dir}/{f}")
        modify_md(f"{path}{title}.md", novel)
        

if __name__ == '__main__':
    main()