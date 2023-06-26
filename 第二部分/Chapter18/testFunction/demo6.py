import pyautogui as gui
from time import sleep


gui.keyDown('command')
gui.keyDown('space')

# 注意抬起来的顺序要和执行的顺序相反
gui.keyUp('space')
gui.keyUp('command')

sleep(1)

gui.typewrite("Momo super Cool~")

exit()