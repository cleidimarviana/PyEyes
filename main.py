import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os


print("Start monitor PyEyes") 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    if os.path.isdir(path):
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()
    else:
        print("\nIncorrect directory or path. Note that it has been entered correctly.")



