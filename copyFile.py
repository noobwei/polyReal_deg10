import os
import shutil
import re


def copy_and_modify_nonce_dirs():
    # 配置路径
    base_code_dir = "baseCode"
    root_dir = "."
    target_filename = "hackPoly.py"
    line_number = 44  # 行号从0开始，第45行对应索引44

    # 遍历根目录下的所有目录
    for dirname in os.listdir(root_dir):
        if dirname.startswith("nonce+"):
            # 解析nonce值（处理可能包含小数点的值）
            match = re.match(r"nonce\+([\d\.]+)", dirname)
            if not match:
                print(f"跳过无效目录名：{dirname}")
                continue

            nonce_value = match.group(1)
            target_dir = os.path.join(root_dir, dirname)
            print(f"\n处理目录: {dirname}")

            # 1. 复制baseCode到目标目录
            print("正在复制基础代码...")
            for item in os.listdir(base_code_dir):
                src = os.path.join(base_code_dir, item)
                dst = os.path.join(target_dir, item)

                if os.path.isdir(src):
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    shutil.copy2(src, dst)
                print(f"已复制: {item}")

            # 2. 修改hackPoly.py
            target_file = os.path.join(target_dir, target_filename)
            if not os.path.exists(target_file):
                print(f"警告：{target_filename} 不存在于 {dirname}")
                continue

            print(f"正在修改 {target_filename}...")
            # 构建替换表达式
            replacement = f"x_values.append({nonce_value})  # 自动替换为 {dirname} 的值"

            # 读取并修改文件
            with open(target_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

                if len(lines) <= line_number:
                    print(f"错误：文件行数不足（需要至少{line_number + 1}行）")
                    continue

                # 修改指定行
                original_line = lines[line_number].rstrip()
                lines[line_number] = replacement + "\n"
                print(f"修改完成：\n原内容: {original_line}\n新内容: {replacement}")

            # 写回文件
            with open(target_file, 'w', encoding='utf-8') as f:
                f.writelines(lines)


if __name__ == "__main__":
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ START PROCESSING ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    copy_and_modify_nonce_dirs()
    print("\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ PROCESS COMPLETED ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("✅ 所有nonce目录已完成代码复制和修改")