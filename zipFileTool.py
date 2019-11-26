import zipfile
from threading import Thread
import sys

def extractFile(zipFile, password):  ###提取文件的类
    try:
        # zipFile.extractall(pwd=bytes(password, "utf8"))  ###打开压缩文件,提供密码...
        zipFile.extractall(pwd=password.encode(encoding='ascii)'))
        print("This file\'s password is " + password)  ###破解到密码
        # 程序退出
        sys.exit(0)
    except Exception as e:
        print(str(e))
        pass  ###假如失败，就跳过继续


def mainStep():
    zipFile = zipfile.ZipFile('./test222.zip')  # 这里的第二个参数用r表示是读取zip文件，w是创建一个zip文件，默认是r
    # 没有密码，解密方法
    # #zipFile.extractall()
    PwdLists = open('./pwd.txt')  # 读入所有密码
    for line in PwdLists.readlines():  # 挨个挨个的写入密码
        Pwd = line.strip('\n')
        # print(Pwd)
        t = Thread(target=extractFile, args=(zipFile, Pwd))
        t.start()

if __name__ == '__main__':
    mainStep()
