# encoding: utf-8
"""
@author: shishengjia
@time: 2017/10/22 下午6:58
"""
import matplotlib.pyplot as plt


class TCPReno:
    """
    td: triple duplicate acknowledgements
    to: timeout
    """

    def __init__(self, ssthresh, td_rounds, to_rounds, total_rounds):
        self.ssthresh = ssthresh
        self.td_rounds = td_rounds
        self.to_rounds = to_rounds
        self.total_rounds = total_rounds
        self.x = [1]
        self.y = [1]

    def draw(self):
        plt.plot(self.x, self.y, marker='o', linestyle='solid')
        plt.yticks([i for i in range(0, 21)])
        plt.xticks([i for i in range(1, self.total_rounds+1)])
        plt.grid()
        plt.show()

    def calculate(self):
        for i in range(2, self.total_rounds+1):

            self.x.append(i)

            # triple duplicate acknowledgements
            if i-1 in self.td_rounds:
                self.ssthresh = self.y[-1] // 2
                self.y.append(self.ssthresh)
                continue

            # timeout
            if i-1 in self.to_rounds:
                self.ssthresh = self.y[-1] // 2
                self.y.append(1)
                continue

            if self.y[-1] < self.ssthresh:  # slow start
                v = self.y[-1] * 2
                if v <= self.ssthresh:
                    self.y.append(v)
                else:
                    self.y.append(self.ssthresh)
            else:  # congestion avoidance
                v = self.y[-1] + 1
                self.y.append(v)

        return self.x, self.y

    def print(self):
        for i in range(len(self.x)):
            print((self.x[i], self.y[i]))


tcp = TCPReno(12, [11], [17], 24)
tcp.calculate()
tcp.print()
tcp.draw()




