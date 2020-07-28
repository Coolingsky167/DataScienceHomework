import numpy as np
import matplotlib.pyplot as plt
def getRadar(data):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    name = ['图结构', '树结构', '数字操作', '排序算法', '查找算法', '字符串', '数组', '线性表']  # 标签
    theta = np.linspace(0, 2 * np.pi, len(name), endpoint=False)  # 将圆根据标签的个数等比分
    value = data
    theta = np.concatenate((theta, [theta[0]]))  # 闭合
    value = np.concatenate((value, [value[0]]))  # 闭合

    ax = plt.subplot(111, projection='polar')  # 构建图例
    ax.plot(theta, value, 'm-', lw=1, alpha=0.75)  # 绘图
    ax.fill(theta, value, 'm', alpha=0.75)  # 填充
    ax.set_thetagrids(theta * 180 / np.pi, name)  # 替换标签
    ax.set_ylim(0, 110)  # 设置极轴的区间
    ax.set_theta_zero_location('N')  # 设置极轴方向
    ax.set_title('编程能力雷达图', fontsize=20)  # 添加图描述
    plt.show()
