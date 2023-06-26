import pyautogui

image_path = '../data/img.png'
locations = pyautogui.locateAllOnScreen(image_path)

for location in locations:
    left, top, width, height = location
    print(f"图像位置：左上角({left}, {top})，宽度：{width}，高度：{height}")
