import time
import threading

flag = False
class MyThread(threading.Thread):
    def run(self):
        print("starting thread")
        global flag
        while True:
            if flag:
                print ("flag is now set")
            time.sleep(1)

printthread = MyThread()
printthread.start()
while True:
    flag = not flag
    time.sleep(5)





