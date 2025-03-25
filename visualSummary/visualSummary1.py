import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('combined_summaries.csv')

# 生成折线图：样本量 vs 攻击成功率
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='SampleSize', y='AvgHitRate',
             estimator='mean', ci=None, marker='o', color='b')
plt.title('Impact of Sample Size on Attack Success Rate')
plt.xlabel('Sample Size')
plt.ylabel('Attack Success Rate')
plt.xticks([5, 10, 20])  # 明确显示实验中的样本量
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()