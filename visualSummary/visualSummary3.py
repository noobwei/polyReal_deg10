import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('combined_summaries.csv')

# 转换为数值类型并排序
df['FitType'] = df['FitType'].astype(float)
sorted_fittypes = sorted(df['FitType'].unique())

# 转换为分类类型保持排序顺序
df['FitType'] = pd.Categorical(
    df['FitType'].astype(str),
    categories=[str(x) for x in sorted_fittypes],
    ordered=True
)

# 创建分面回归图
g = sns.lmplot(data=df, x='NonceMax', y='AvgHitRate', col='FitType',
               col_order=[str(x) for x in sorted_fittypes],  # 确保排序顺序
               col_wrap=3, height=4, aspect=1.2,
               scatter_kws={'alpha':0.4, 's':60},
               line_kws={'color':'red', 'lw':1.5})

# 设置标题和标签
g.set_titles("FitType: {col_name}")
g.set_axis_labels("NonceMax (Larger Value = Wider Range)", "Attack Success Rate")
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Combined Impact of Nonce Range and Fit Type on Success Rate', y=1.02)

# 格式化坐标轴
for ax in g.axes.flat:
    ax.grid(alpha=0.3)
    ax.set_xticks([0, 500, 1000, 1500, 2000])
    ax.set_xticklabels(['0', '500', '1000', '1500', '2000'])

plt.tight_layout()
plt.show()