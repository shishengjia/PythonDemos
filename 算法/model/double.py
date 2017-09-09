import matplotlib.pyplot as plt


def generate_pics():
    for i in range(1, 5):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        fig = plt.figure(str(i))
        #...

    plt.show()