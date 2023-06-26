#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        # 获取鼠标的位置，然后输出出来
        x, y = pyautogui.position()
        position: str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        # 获取鼠标当前所在位置的颜色
        screen_img = pyautogui.screenshot()
        pixel_color = screen_img.getpixel((x, y))     # 获取所在位置的 RGBA 值
        # 坐标输出后面再加上新的内容
        position += ' RGB: (' + str(pixel_color[0]).rjust(3)
        position += ', ' + str(pixel_color[1]).rjust(3)
        position += ', ' + str(pixel_color[2]).rjust(3) + ')'

        # 这个 position 是格式好的字符串
        # 为了每一次的输出都是刷新的显示，我们要退掉之前输入的，所以不能换行
        print(position, end='')
        # 去除掉之前的字符串输出，让新的字符串显示在那个位置
        print('\b' * len(position), end='', flush=True)

except KeyboardInterrupt:
    print("\nDone!")
