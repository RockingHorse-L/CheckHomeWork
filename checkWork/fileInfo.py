"""
    读取作业存放的文件
        fileWork = os.listDir()
            for file in fileWork:
        将遍历的结果存放到列表里
        fileWork=List = []
        fileWorkList.append(file)
    读取name文件
        fileName = open('name.txt', 'r', encoding='utf-8')
        fileNameInfo = fileName.readLines(fileName)
            for name in fileNameInfo:
                在遍历name的时候直接进行字符串的比对
                    a = 'abcdefg'
                    b = 'bcd'
                    c = 'fgh
                    print(a.find(b))
                    print(a.find(c))
                    输出1和-1


"""
import os


def checkWork(path, file):
    """
    检查谁没交作业
    :param path: 微信文件存放地址
    :param file: 名字文档
    :return:
    """
    fileWork = os.listdir(path)
    fileName = open(file, 'r', encoding='utf-8')
    fileNameInfo = fileName.readlines()
    nameList = []


    for names in fileNameInfo:
        names = names.strip().replace('\n', '')
        nameList.append(names)

    flag = 0
    for name in nameList:
        for i in range(len(fileWork)):
            if name in fileWork[i]:
                flag = 1
                break
            else:
                flag = -1
        if flag == -1:
            print(f'{name}没交作业')



path = 'C:/Users/Yaogun-Ma/Documents/WeChat Files/wxid_md1iro922pya22/FileStorage/File/2023-04'
file = 'name.txt'
checkWork(path, file)