import os
import pandas as pd
from pathlib import Path


def extract_fit_type(folder_name):
    """从文件夹名称中提取拟合类型（nonce值）"""
    if folder_name.startswith("nonce+"):
        return float(folder_name.split("+")[1])
    return None


def process_summaries(root_dir, output_file="combined_summaries.csv"):
    # 创建空DataFrame存储结果
    combined_df = pd.DataFrame()

    # 遍历根目录下的所有子目录
    for folder in os.listdir(root_dir):
        folder_path = Path(root_dir) / folder

        # 只处理以"nonce+"开头的目录
        if folder.startswith("nonce+") and folder_path.is_dir():
            fit_type = extract_fit_type(folder)
            if fit_type is None:
                continue

            # 查找所有summary文件
            summary_files = folder_path.glob("summary_*.csv")

            for csv_file in summary_files:
                try:
                    # 读取CSV文件，仅保留需要的列
                    df = pd.read_csv(
                        csv_file,
                        usecols=["NonceMin", "NonceMax", "SampleSize", "AvgHitRate"]
                    )

                    # 添加拟合类型列
                    df["FitType"] = fit_type

                    # 追加到结果集
                    combined_df = pd.concat([combined_df, df], ignore_index=True)

                except Exception as e:
                    print(f"Error processing {csv_file}: {str(e)}")

    # 保存最终结果
    combined_df.to_csv(output_file, index=False)
    print(f"Combined data saved to {output_file}")
    return combined_df


if __name__ == "__main__":
    # 设置项目根目录（根据实际路径修改）
    project_root = os.getcwd()

    # 执行处理
    process_summaries(project_root)