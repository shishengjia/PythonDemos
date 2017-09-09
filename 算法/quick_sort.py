# # coding:utf-8
# # 快速排序
#
#
# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i < pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort([1, 11, 6, 13, 4]))
#
import matplotlib.pyplot as plt


# def calculate(begin, end, price):
#     begin_end = zip(begin, end)
#     print(begin_end)
#     d_value = [y-x for x, y in begin_end]
#     print(d_value)
#     total_price = [x*price for x in d_value]
#     print(total_price)
#
# calculate([2322, 2312, 2327], [2345, 2366, 2346], 0.9)
#
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# labels = [u'施圣佳 60元', u'徐海涛 60元', u'郭亮 60元', u'姚远 60元', u'赵涵宇 60元', u'徐健翔 60元']
# X = [60, 50, 70, 80, 65, 77]
#
# fig = plt.gcf()
# # 尺寸
# fig.set_size_inches(6, 4)
# fig.dpi = 100
#
# _, out_text, inner_text = plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
# print(out_text, inner_text)
#
# plt.title("文昌楼12F/45 水电费")
# plt.axis('equal')
# # plt.legend()
# # plt.show()
#
# plt.legend(loc=0, numpoints=1)
# leg = plt.gca().get_legend()
# legend_text = leg.get_texts()
#
# # 图例文字大小
# plt.setp(legend_text, fontsize='xx-small')
# # 饼图外部文字大小
# plt.setp(out_text, fontsize='small')
# # 饼图内部文字大小
# plt.setp(inner_text, fontsize='small')

for i in range(1, 5):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    labels = [u'施圣佳 60元', u'徐海涛 60元', u'郭亮 60元', u'姚远 60元', u'赵涵宇 60元', u'徐健翔 60元']
    X = [60, 50, 70, 80, 65, 77]

    fig = plt.figure(str(i))
    # 尺寸
    fig.set_size_inches(6, 4)
    fig.dpi = 100

    _, out_text, inner_text = plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
    print(out_text, inner_text)

    plt.title("文昌楼12F/45 水电费")
    plt.axis('equal')
    # plt.legend()
    # plt.show()

    plt.legend(loc=0, numpoints=1)
    leg = plt.gca().get_legend()
    legend_text = leg.get_texts()

    # 图例文字大小
    plt.setp(legend_text, fontsize='xx-small')
    # 饼图外部文字大小
    plt.setp(out_text, fontsize='small')
    # 饼图内部文字大小
    plt.setp(inner_text, fontsize='small')

plt.show()
