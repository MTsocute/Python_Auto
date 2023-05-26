#! python3
"""
    1.用户输入 save 命令时，剪贴板的内容存储到 shelf 文件中
    2.用户输入 list 命令时，shelf 所有关键词存储到剪贴板中
    3.用户输入 关键字 的时候，就先去找找 shelf 没有没有这个关键字
        1. 有的话，就把 shelf 关键词下内容拷贝到剪贴板
        2. 没的话，就拉倒吧
"""

import shelve, pyperclip, sys

# 要记得 mcbShelf 是采用和字典一样的存储模式的二进制文件
mcbShelf = shelve.open('/Users/momo/Desktop/Python_Auto/第二部分/Chapter8/data/mcb')

""" Save Clip's content into shelf """

# 我们输入的命令是：python3 mcb.pyw save keyword
# sys.arg 就会是：[mcb.pyw, save, keyword]
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # 保存剪贴板内容到 mcShelf['spam'] spam 这个关键字的空间中
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print("Content of Clipboard has been saved.")
elif len(sys.argv) == 2:
    # 当命令是 list 时
    if sys.argv[1].lower() == 'list':
        if len(list(mcbShelf.keys())) == 0:
            print("There is not keyword in shelf file!")
            print("Please use \"python3 mcb.py save keyword\" to store clipboard content into shelf file.")
        # 枚举 shelf 文件中的关键词，打印到终端
        else:
            print(str(list(mcbShelf.keys())))
    # 对应 说明3 部分
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print('KeyWord Not Found!!!')

mcbShelf.close()