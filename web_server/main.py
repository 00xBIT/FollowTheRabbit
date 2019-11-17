import threading
import json
import os

import webServerStarter

import json
import time

def loop():
    while True:
        time.sleep(1)
        # print("loop")

if __name__ == "__main__":
    from sys import argv
    print(argv)

    __CONFIG_FOLDER = 'config'
    __CONFIG_FILE = 'config.json'

    configs = {}
    configPath = __CONFIG_FOLDER + '/' + __CONFIG_FILE
    if os.path.exists(configPath):
        with open(configPath, 'rb') as f:
            configs = json.loads(f.read())

    INCOMING_REQUESTS_FOLDER = 'INCOMING_REQUESTS'
    try:
        os.mkdir(INCOMING_REQUESTS_FOLDER)
    except OSError:
        print("Creation of the directory %s failed" % INCOMING_REQUESTS_FOLDER)
    else:
        print("Successfully created the directory %s " % INCOMING_REQUESTS_FOLDER)

    # sender = sender.Sender(configs)
    # senderThread = threading.Thread(target=sender.start)
    # senderThread.start()
    # Heroku app need a loop for woking nonstop
    threading.Thread(target=loop).start()

    if len(argv) == 2:
        webServerStarter.run(int(argv[1]))
    else:
        webServerStarter.run(8080)