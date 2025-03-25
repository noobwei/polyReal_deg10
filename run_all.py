import os
import subprocess
import sys


def run_experiments():
    folders = [
        "nonce+0",
        "nonce+2",
        "nonce+2.4",
        "nonce+2.46",
        "nonce+2.467",
        "nonce+2.4675"
    ]

    for folder in folders:
        print(f"\n=== 开始执行 {folder} ===")

        # 构建路径
        folder_path = os.path.join(os.getcwd(), folder)
        script_path = os.path.join(folder_path, "run_experiments.py")

        # 路径验证
        if not os.path.exists(script_path):
            print(f"错误: {script_path} 不存在")
            continue

        # 执行脚本
        try:
            subprocess.run(
                [sys.executable, "run_experiments.py"],
                cwd=folder_path,
                check=True
            )
            print(f"完成 {folder}")
        except subprocess.CalledProcessError:
            print(f"执行失败: {folder}")
        except Exception as e:
            print(f"意外错误: {str(e)}")


if __name__ == "__main__":
    print("启动批量执行")
    run_experiments()
    print("\n所有任务执行结束")