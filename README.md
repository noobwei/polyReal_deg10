## 基础结构与参数

基础代码的结构如下

```
├── baseCode/
│   ├── DataGen.py
│   ├── hackPoly.py
│   ├── hackVerifier.py
│   └── run_experiments.py
```

DataGen用于生成100000个数据，用作数据集，这里代码中使用的是**正态分布**并且使用**真实数据的参数**进行数据生成，可以指定所有数据的数据精度（小数点后几位）。另外为了评估nonce取值大小对攻击者成功率的可能影响，**nonce的可能最大最小取值**也作为参数，但实际参数由后续的运行脚本传入。

hackpoly则通过在数据集中随机抽取**一定量**的数据进行多项式的拟合，而因为攻击假设中攻击者不知道所有传感器response分布的均值，所以在后续试验中设定**不同精度的均值猜测**如nonce+0，nonce+2，nonce+2.4依次类推，在每一次攻击（拟合）流程后，均会保存结果至result中，包括取样数，实验ID，以及对应的所有参数。因为随机抽取sample有非常大的随机性，所以**随机试验次数**也作为变量之一。

hackverifier通过读取hackpoly产出的result，使用完整数据集进行验证，原理为使用y和拟合出的多项式参数反推出x‘+nonce，并且利用已知nonce获得x’并验证其是否在x的**期待阈值**内。hackverifier会计算出整体攻击（验算）成功率并且将结果存入summary

run_experiments即运行所有攻击和验算流程的自动脚本，其中有效参数是**nonce的范围**，samples似乎不能有效传入，建议修改逻辑。

所有的csv结果输出均以nonce的取值范围为基准命名。

下面对可以修改的参数进行汇总

1. DataGen 

   - L48-49可以修改分布的参数

   - L95-101可以修改数据精度设置

2. hackPoly
   - L81**可能**可以真实设置实验sample数量
   - L82可以设置随机抽取实验的次数
3. hackVerifier
   - L8可以设置验证阈值
   - L78**可能**设置参与验证的随机抽取实验的次数

4. run_experiments
   - L5-L17可以设置nonce的取值范围

## 实验流程

在实验时候，需要手动复制baseCode并修改关键参数，按照nonce+n（n为攻击者猜测所有传感器分布均值）命名文件夹名

除了baseCode外，其他代码可以考虑复用，作用为

- summarySummary：读取所有nonce+n中的summary内容，并输出总summary csv
- visualDir：输出文件夹完整路径可视化，适用于作为prompt给大语言模型debug
- **run_all**：如果能确保代码持续运行，可以直接运行所有nonce开头文件夹中的run_experiments，运行所有实验

另外修改最高阶数可能略微复杂，修改参数较多，建议参考deg10和原始repo中代码区别。
