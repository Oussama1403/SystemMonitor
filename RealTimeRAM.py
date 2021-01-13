import psutil
import time
#Cancel Program by pressing Ctrl+C
print("Ctrl+C to exit.")

def Status():
    while True:
        print("RAM percent :",psutil.virtual_memory().percent,"%",end='')
        print(" | Available RAM :",psutil.virtual_memory().available/1024,end='')
        print(" | Used RAM :",psutil.virtual_memory().used/1024,end='\r')
        time.sleep(1)
Status()        
