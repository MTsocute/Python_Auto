#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re

# 创建电话的正则表达式
# 美国电话号码的结构：(area code)-***-****，中间的分隔符号可以是空格 - .
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # Area code:区号是可有可无的，所以要跟问号
    (\s|-|\.)?              # Separator：分隔符号一般是 空格 短横 逗号，如果区号没有那也没有，所以跟问号
    (\d{3})                 # First 3 digits of phone number
    (\s|-|\.)               # separator
    (\d{4})                 # last 4 digits of phone number
    # extension:可选的分机号，包括任意数目的空格， 接着 ext、x 或 ext点，任意空白，再接着 2 到 5 位数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  
)''', re.VERBOSE)

# TODO: Create email regex.
# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @[a-zA-Z0-9.-]+         # @domain
    (\.[a-zA-Z]{2,4})       # .xxx
)''', re.VERBOSE)


# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())    # 拷贝剪贴板的内容

# 混合的装载着邮箱和电话
matches = []

# 找到剪贴板中的所有的电话：返回的是一个元组
for groups in phoneRegex.findall(text):
    # 把关键的电话号码组合起来
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    # 处理有拓展号的电话
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    # 电话号码放到数组中去
    matches.append(phoneNum)

# 匹配所有的邮箱号码
for groups in emailRegex.findall(text):
    matches.append(groups[0])   # 第一个元素就是整体的邮箱

# TODO: Copy results to the clipboard.
if len(matches) > 0:
    # 匹配到的电话、邮箱整合成一个字符串换行
    pyperclip.copy('\n'.join(matches))
    # 提示用户已经查询到的邮箱和手机整理好存储到剪贴板中了
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')