# จากไลบรารี threading นำเข้าคลาส Thread และ time เพื่อใช้ในโปรแกรม
from threading import Thread
import time

# สร้างคลาส myThread โดยสืบทอดมาจาก Thread
class myThread(Thread):
    # เมธอด __init__ เป็นเมธอดที่ถูกเรียกเมื่อสร้างอ็อบเจกต์ของคลาส
    def __init__(self, threadID, name, counter):
        # เรียกเมธอด __init__ ของคลาสแม่ (Thread) ด้วย super() เพื่อกำหนดค่าเริ่มต้น
        Thread.__init__(self)
        # กำหนดค่าตัวแปรให้กับอ็อบเจกต์
        self.threadID = threadID
        self.name = name
        self.counter = counter

    # เมธอด printTime เพื่อพิมพ์เวลาของ thread ที่กำลังทำงาน
    def printTime(self, threadName, delay, counter):
        while counter:
            time.sleep(delay)  # หยุดการทำงานตามเวลาหน่วงที่กำหนด (delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))  # พิมพ์เวลาปัจจุบัน
            counter -= 1

    # เมธอด run เมื่อเริ่มทำงาน Thread จะเรียกเมธอดนี้
    def run(self):
        print("Starting " + self.name)
        # เรียกเมธอด printTime เพื่อพิมพ์เวลาของ thread ที่กำลังทำงาน 5 ครั้ง
        self.printTime(self.name, self.counter, 5)
        print("Exiting " + self.name)

# สร้างอ็อบเจกต์ของคลาส myThread สองตัว แยกตามชื่อและค่าเวลาหน่วงการทำงาน
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# เริ่มการทำงานของทั้งสอง Thread โดยใช้เมธอด start()
thread1.start()
thread2.start()
