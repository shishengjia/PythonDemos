

"""
处理时间记录格式，统一为min:sec格式
"""
def deal_string(time_string):
    if "-" in time_string:
        return time_string.replace("-", ":")
    elif "." in time_string:
        return time_string.replace(".", ":")
    else:
        return time_string


class AthleteList(list):
    """
    继承list
    """
    def __init__(self, name='', record=[]):
        list.__init__([])
        self.name = name
        self.extend(record)

    def get_data(self, filename):
        """
        获取文件里的数据
        """
        try:
            with open(filename, "r") as reader:
                athlete_list = []
                for line in reader:
                    # 按照格式取出姓名和成绩
                    name, record = line.split(":", 1)
                    # 先对成绩格式进行处理，先取出空白字符，再以","分割数据
                    record = record.strip().split(",")
                    # 对成绩表示格式进行统一
                    record_ = list(map(lambda x:deal_string(x), record))
                    athlete_list.append(AthleteList(name, record_))
                return athlete_list
        except IOError as err:
            print("FileError" + str(err))
            return None

    def get_Top3(self, data):
        return sorted(set(data))[:3]


data = AthleteList().get_data("records.txt")
print(data[0].name, data[0].get_Top3(data[0]))
print(data[1].name, data[1].get_Top3(data[1]))











# 项目概述
# 目标/背景
# 系统分析
# ER图/功能结构图
#
#
# 系统设计
