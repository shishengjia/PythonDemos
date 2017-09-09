# coding:utf-8


class Solution:
    def jingzhi_transfer(self, number, n):
        """
        number化成n进制后各个位的数字及其和
        """
        m = number // n
        l = []
        sum = 0
        while m != 0:
            l.append(number % n)
            sum += number % n
            m = number = number//n
        return sum

    def gcd(self, a, b):
        """
        辗转相除法求最大公约数
        """
        while a % b:
            c = a % b
            a = b
            b = c
        return b

    def main(self, number):
        sum = 0
        for i in range(2, number):
            sum += self.jingzhi_transfer(number, i)

        d = self.gcd(sum, number - 2)
        print(str(sum // d) + '/' + str((number - 2) // d))

S = Solution()
# 字符串转为list
number = int(input())
if number is not None:
    S.main(number)



