import time
import sys
import os
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import LoggingEventHandler
import logging

class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):

        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
       
        path = sys.argv[2] if len(sys.argv) > 1 else '.'

        if os.path.isdir(path):

            event_h = LoggingEventHandler()
            self.observer.schedule(event_h, path, recursive=True)
            self.observer.start()
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt :
                self.observer.stop()
                print("\nThere was an error trying to get an eagle view.")

            self.observer.join() 
        else:
            print("\nIncorrect directory or path. Note that it has been entered correctly.")         

if __name__ == '__main__':    
    w = Watcher()    
    w.run()
