import os
import shutil


def clean_nonce_dirs(root_dir='.'):
    """删除所有以nonce+开头的文件夹内的文件"""
    for entry in os.listdir(root_dir):
        if entry.startswith("nonce+") and os.path.isdir(entry):
            dir_path = os.path.join(root_dir, entry)
            print(f"Cleaning directory: {dir_path}")

            # 遍历目录内容
            for item in os.listdir(dir_path):
                item_path = os.path.join(dir_path, item)

                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.remove(item_path)  # 删除文件或符号链接
                        print(f"Deleted file: {item_path}")
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)  # 递归删除子目录
                        print(f"Deleted directory: {item_path}")
                except Exception as e:
                    print(f"Failed to delete {item_path}: {e}")


if __name__ == "__main__":
    # 使用示例（默认清理当前目录）：
    clean_nonce_dirs()

    # 如果要指定其他目录，可以这样使用：
    # clean_nonce_dirs("/path/to/your/directory")