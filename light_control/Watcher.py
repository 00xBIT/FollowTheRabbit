import time
import requests
import json

url = "https://junction-webserver.herokuapp.com/"

class Watcher():
    __isSwitchOn1 = False
    __isSwitchOn2 = False

    def __init__(self):
        pass

    def start(self):
        while True:
            try:
                print("Watcher: send get request...")
                responce = requests.get(url)
                if responce.status_code != 200:
                    print("responce.status_code = %i", responce.status_code)

                print("Watcher: responce recived.")
                data = json.loads(responce.text)

                if data:
                    switchOn1 = 'switchOn1'
                    if switchOn1 in data:
                        print("Watcher: switchOn1 is " + str(data[switchOn1]))
                        self.__isSwitchOn1 = bool(data[switchOn1])

                    switchOn2 = 'switchOn2'
                    if switchOn2 in data:
                        print("Watcher: switchOn2 is " + str(data[switchOn2]))
                        self.__isSwitchOn2 = bool(data[switchOn2])
                else:
                    print("Watcher: data is empty")
                
                time.sleep(1)
            except:
                print("Watcher: Unexpected error")

    def isSwitchOn1(self):
        return self.__isSwitchOn1

    def isSwitchOn2(self):
        return self.__isSwitchOn2