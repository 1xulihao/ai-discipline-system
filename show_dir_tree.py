import os

def print_directory_tree(start_path, indent=''):
    for item in os.listdir(start_path):
        path = os.path.join(start_path, item)
        if os.path.isdir(path):
            print(f"{indent}📁 {item}/")
            print_directory_tree(path, indent + '    ')
        else:
            print(f"{indent}📄 {item}")

if __name__ == "__main__":
    project_path = input("请输入项目目录路径（例如 E:/learn/lanzhao/ai-discipline-system）：\n").strip()
    if os.path.exists(project_path):
        print(f"\n项目结构 @ {project_path}：\n")
        print_directory_tree(project_path)
    else:
        print("❌ 路径不存在，请检查路径是否正确。")
