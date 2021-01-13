import psutil
import threading
import time
#Cancel Program by pressing Ctrl+C

def RamStatus():
    while True:
        current = psutil.virtual_memory().used/1024
        print("RAM percent :",psutil.virtual_memory().percent,"%",end='')
        time.sleep(1)

def AvailableRam():
    while True:
        print(" | Available RAM :",psutil.virtual_memory().available/1024,end='')
        time.sleep(1)
def UsedRam():
    while True:
        print(" | Used RAM :",psutil.virtual_memory().used/1024,end='\r')
        time.sleep(1)
     
th1 = threading.Thread(target=RamStatus)
th2 = threading.Thread(target=AvailableRam)
th3 = threading.Thread(target=UsedRam)

th1.start()
th2.start()
th3.start()


