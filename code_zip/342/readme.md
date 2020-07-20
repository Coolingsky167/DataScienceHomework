### 题目描述

您需要写一种数据结构（可参考题目标题），来维护一个序列，其中需要提供以下操作：

翻转一个区间，例如原有序序列是 5 4 3 2 1，翻转区间是[2,4]的话，结果是 5 2 3 4 1。
### 输入描述

```
第一行为年n,m，n表示初始序列有n个数，这个序列依次是{1,2,...,n-1,n}，m表示翻转操作次数。
接下来m行每行两个数[l,r]，数据保证1≤l≤r≤n。
```
### 输出描述

```
输出一行n个数字，表示原始序列经过m次变换后的结果。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 3
1 3
1 3
1 4
```
```
4 3 2 1 5
```