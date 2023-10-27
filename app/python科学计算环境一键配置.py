import os
import importlib
import importlib.util

def is_load(name):
    result=importlib.util.find_spec(name)
    return result is not None

print("请确保已将python和pip配置到全局变量中，否则程序将运行失败\n作者：ICTA会长HonmaKohaku")
x=input("是否开始进行环境配置（Y/N）：")
while x=='Y':
    choose=input("输入数字选择要进行的程序\n1.numpy\n2.matplotlib\n3.pandas\n4.sympy\n5.scipy\n6.天文学，生物学库\n7.查询库状态\n8.更新pip(建议先进行):\n9.退出\nEnter the number you chosed:")
    if float(choose)==1:
        os.system(f'cls')
        os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy')
        if is_load('numpy'):
            print('numpy 安装成功')
        else:
            print('numpy安装失败')
    elif float(choose)==2:
        os.system(f'cls')
        os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib')
        if is_load('matplotlib'):
            print('matplotlib安装成功')
        else:
            print('matplotlib安装失败')
    elif float(choose)==3:
        os.system(f'cls')
        os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas')
        if is_load('pandas'):
            print('pandas安装成功')
        else:
            print('pandas安装失败')
    elif float(choose)==4:
        os.system(f'cls')
        os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sympy')
        if is_load('sympy'):
            print('sympy安装成功')
        else:
            print('sympy安装失败')
    elif float(choose)==5:
        os.system(f'cls')
        os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scipy')
        if is_load('scipy'):
            print('scipy安装成功')
        else:
            print('scipy安装失败')
    elif float(choose)==6:
        os.system(f'cls')
        os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple astropy')
        os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple biopython')
        if is_load('astropy'):
            print('astropy安装成功')
        else:
            print('astropy安装失败')
        if is_load('Bio'):
            print('Biopython安装成功')
        else:
            print('Biopython安装失败')
    elif float(choose)==7:
        os.system(f'cls')
        for i in ('numpy','matplotlib','pandas','sympy','scipy','astropy','Bio'):
            if is_load(i):
                print(i+'已安装')
            else:
                print(i+'未安装')
    elif float(choose)==8:
        os.system(f'cls')
        os.system(f'python.exe -m pip install --upgrade pip')
    elif float(choose)==9:
        quit()
    else:
        os.system(f'cls')
        print("请输入正确的号码！！")
