import os
import re


def transform(localfile=r'.\cases'):
    """
    对当前目录的cases文件夹下的
    py文件转换为robot文件
    """
    # 查找当前目录的所有文件和文件夹
    for root, dirName, file in os.walk(localfile, topdown=False):

        # 对所有文件进行判断
        for name in file:
            # 分离文件名和后缀
            realName = os.path.splitext(name)
            if realName[1] == '.py':
                # 初始化文件检查
                if name == '__st__.py':
                    oName = root + r'\__init__.robot'
                    sName = root + r'\__st__.py'
                    with open(oName, 'w+', encoding='utf-8') as init:
                        init.write('*** Settings ***\n')
                        init.write('\nLibrary  ' + '\t' + name + '\t' + 'WITH NAME' + '\t'+'M'+'\n')
                        fileTransform(sName, init, realName[0], st=True)
                else:
                    # 套件检查

                    oName = root+'\\' + realName[0] + '.robot'
                    sName = root + '\\' + name
                    with open(oName, 'w+', encoding='utf-8') as ofile:
                        ofile.write('*** Settings ***\n')
                        ofile.write('\nLibrary  ' + '\t'+name + '\t' + 'WITH NAME' + '\t'+'M'+'\n')
                        fileTransform(sName, ofile, realName[0])
    return '转换成功'


def fileTransform(sfilePath, fileWritePath, realName, st=False):
    """
    测试用例转换为RF能识别的格式

    参数：
    sfilePath:要转换文件路径
    fileWritePath:需写入的的文件对象
    realName:写入文件名
    st:是否是初始化文件
    """

    # 读取文件
    textHeader = []
    if not st:
        textBody = ['*** Test Cases ***', '\r']
    else:
        textBody = []
    with open(sfilePath, 'r', encoding='utf-8') as s1file:
        # 识别并转换
        for line in s1file.readlines():
            # 测试用例导入
            C1 = re.search(r'class\s*(C\d+)\s*:', line, re.I)
            if C1:
                C = C1.group(1)
                textHeader.append('\nLibrary  ' + '\t' + realName + '.' + C + '\t'+'WITH NAME' + '\t'+C+'\n')
            # 用例文件标签
            Tas = re.search(r'force_tags\s*=\s*(\[.*\])', line, re.I)
            if Tas:
                temp1 = Tas.group(1)
                temp2 = '\t'.join(eval(temp1))
                textHeader.append('\n' + 'Force Tags' + '\t' + temp2 + '\n')
            # 单个测试套件的初始化
            s = re.search(r'def\s*(suite_setup)', line, re.I)
            if s:
                textHeader.append('\n'+'Suite Setup    M.suite_setup'+'\n')
            t = re.search(r'def\s*(suite_teardown)', line, re.I)
            if t:
                textHeader.append('\n'+'Suite Teardown    M.suite_teardown'+'\n')
            # 用例名
            N1 = re.search(r"name\s*=\s*(\'.*\')", line)
            # name = ' '
            if N1:
                N = N1.group(1)
                textBody.append('\n' + N + '\n')
            # 单个用例初始话
            S = re.search(r'def\s*(setup)', line, re.I)
            if S:
                textBody.append(r'  [Setup]' + '    ' + C + '.setup' + '\n')
            T = re.search(r'def\s*(teardown)', line, re.I)
            if T:
                textBody.append(r'  [Teardown]' + '    ' + C + '.teardown' + '\n')
            # 标签
            TA = re.search(r'(?<!_)tags\s*=\s*(\[.*\])', line)
            if TA:
                temp1 = TA.group(1)
                temp2 = '\t'.join(eval(temp1))
                textBody.append('\n'+'  ' + '[Tags]' + '\t' + temp2 + '\n')
            # 用例
            TS = re.search(r'def\s*(teststeps)', line, re.I)
            if TS:
                TS = TS.group(1)
                textBody.append('\n  ' + C + '.' + TS + '')
        for i in textHeader:
            fileWritePath.write(i)

        for j in textBody:
            fileWritePath.write(j)


if __name__ == '__main__':
    print(transform())