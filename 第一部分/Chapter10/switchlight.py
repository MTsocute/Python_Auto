def switchLights(stoplight):
    """
        代码潜在问题，就是无法确保红灯数量，如果都是路灯就会撞车了
    """
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'

        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'

        elif stoplight[key] == 'red':
            stoplight[key] = 'green'


if __name__ == '__main__':
    pass
