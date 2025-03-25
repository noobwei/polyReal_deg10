import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('combined_summaries.csv')

plt.figure(figsize=(10,6))
# 使用条形图展示不同FitType的精度等级
sns.barplot(data=df, x='FitType', y='AvgHitRate', ci=None)
plt.title('Impact of Attacker Precision (FitType) on Success Rate')
plt.xlabel('FitType (Higher Value = More Precise)')
plt.ylabel('Attack Success Rate')
plt.xticks(rotation=45)  # 旋转标签避免重叠
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()