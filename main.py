import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import datetime
import webbrowser


print("\n ----------------------\n| Start monitor PyEyes |\n ----------------------") 

class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        path = sys.argv[1] if len(sys.argv) > 1 else '.'

        if os.path.isdir(path):
            event_handler = LoggingEventHandler()
            self.observer.schedule(event_handler, path, recursive=True)
            self.observer.start()
            self.renewPage(logging)
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.observer.stop()
                self.observer.join()
        else:
            print("\nIncorrect directory or path. Note that it has been entered correctly! :-(")
        

    def renewPage(self, text):
        f = open('helloworld.html','w')

        message = """<html>
        <head></head>
        <body><p>{text}</p></body>
        </html>"""

        f.write(message)
        f.close()
        return webbrowser.open_new_tab('helloworld.html')

if __name__ == "__main__":
    w = Watcher()
    w.run()

