#!/opt/homebrew/bin/python3
import sys
import pyperclip

PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}


""" 
    获取外面一个参数，这个参数是账号，然后返回对应的密码到剪贴板 
    sys.argv 返回一个列表中:
        第一项总是一个字符串，它包含程序的文件名('pw.py')。
        第二项应该是第一个命令行参数
        第三项到第n项，就是参数的个数决定的
"""

if len(sys.argv) < 2:   # 如果我们忘记输入参数[账号]，那就是少输入一个参数
    print("您缺少了 [账号] 这个参数！")
    print('使用方法: python3 pw.py [所需的账号] - 就会返回对应的密码到剪贴板')
    sys.exit()

account = sys.argv[1]   # 显示第二项：命令行参数
print(f'检测用户输入到：{account}')    # 把我们命令行输入的参数打印出来


if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print(f'{account} 密码已经拷贝到剪贴板当中了!')
else:
    print("检无此账号！！！")
