import threading
import time


def take_a_nap():
    print('Sleeping...\n')
    time.sleep(2)
    print("Wake up\n")


# 程序一旦进入 sleep 就会调用线程
threadObj = threading.Thread(target=take_a_nap)
# 执行线程
threadObj.start()

print("This is the end of program...\n")
