def boxprint(symbol: str, width: int, height: int) -> None:
    """
        它接受一个字符、一个宽度和一个长度
        它按照指定的长和宽，用该字符创建了一个小盒子的图像
        但是我们限定 长和宽度必须 > 2 不然就报错
    """
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    # 绘制图形
    Draw(symbol, width, height)


def Draw(symbol: str, width: int, height: int):
    """
        实现字符创建了一个小盒子的图像
    """
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


def ts_demo() -> None:
    """
        用于测试 import 是否正常
    """
    print("You motherfucker!")


if __name__ == '__main__':
    boxprint('*', 4, 4)
