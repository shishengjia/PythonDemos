# encoding: utf-8
"""
@author: shishengjia
@time: 2017/10/12 下午3:29
"""
from matplotlib import pyplot as plt


x = [1, 2, 3]
y = [2, 3, 4]

plt.figure()

plt.subplot(231)
plt.plot(x, y)

plt.subplot(232)
plt.bar(x, y)


# plt.subplot(233)
#
# plt.subplot(234)
#
# plt.subplot(235)
#
# plt.subplot(236)

plt.show()




