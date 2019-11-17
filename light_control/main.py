import threading
import time

import MyLightControl
import Watcher

if __name__ == "__main__":
    from sys import argv
    print(argv)

    control = MyLightControl.MyLightControl()

    watcher = Watcher.Watcher()
    watcherThread = threading.Thread(target=watcher.start)
    watcherThread.start()

    while True:
        if watcher.isSwitchOn1():
            control.blink()
        else:
            control.setOff()
        
        if watcher.isSwitchOn2():
            control.finishLightOn()
        else:
            control.finishLightOff()
            
        time.sleep(0.1)
