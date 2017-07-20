import pickle
man = []
others = []
try:
    data = open("test.txt")
    for line in data:
        try:
            role, conetnt = line.split(":")
            if role.strip() == "Man":
                man.append(conetnt.strip())
            else:
                others.append(conetnt.strip())
        except ValueError:
            pass
    data.close()

except IOError:
    print("The file does not exist")

try:
    with open("man_.txt", "wb") as manw, open("others_.txt", "wb") as othersw:
        pickle.dump(man, manw)
        pickle.dump(others, othersw)
except IOError as err:
    print("Error:" + str(err))

try:
    with open("man_.txt", "rb") as reader:
        new_man = pickle.load(reader)
        print(new_man)
except IOError as err:
    print("FileError" + str(err))
