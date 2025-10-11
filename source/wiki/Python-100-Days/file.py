import os

def list_files_by_directory(root_dir):
    """
    遍历文件夹，整理文件结构
    
    Args:
        root_dir: 要遍历的根目录路径
    """
    file_structure = {}
    
    # 遍历根目录下的所有条目
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        
        # 如果是文件夹
        if os.path.isdir(item_path):
            folder_name = f"'{item}'"
            file_structure[folder_name] = []
            
            # 遍历文件夹内的文件
            for file_item in os.listdir(item_path):
                file_path = os.path.join(item_path, file_item)
                if os.path.isfile(file_path):
                    file_structure[folder_name].append(f"- {file_item}")
    
    return file_structure

def print_file_structure(file_structure):
    """打印文件结构"""
    for folder, files in file_structure.items():
        print(f"  {folder}:")
        for file in files:
            print(f"    {file}")

# 使用示例
if __name__ == "__main__":
    root_directory = "D:\code\stellar\source\wiki\Python-100-Days"  # 当前目录，可以修改为你的目标目录
    structure = list_files_by_directory(root_directory)
    print_file_structure(structure)