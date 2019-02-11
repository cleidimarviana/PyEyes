import time
import sys
import os
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import LoggingEventHandler

class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        if len(sys.argv) > 1:

            path = sys.argv[1]

            if os.path.isdir(path):

                event_h = Handler()
                self.observer.schedule(event_h, path, recursive=True)
                self.observer.start()
                                
                try:
                    while True:
                        time.sleep(1)
                except :
                    self.observer.stop()
                    print("\nThere was an error trying to get an eagle view.")

                self.observer.join() 
            else:
                print("\nIncorrect directory or path. Note that it has been entered correctly.")         
        else:
            print('\nWithout any argument I do not work.') 

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print (now+ " -> Created: " + event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print (now+ " -> Modified: " + event.src_path)
        
        elif event.event_type == 'deleted':
            # Taken any action here when a file is deleted.
            print (now + " -> Deleted: " + event.src_path)
       
        elif event.event_type == 'moved':
            # Taken any action here when a file is renamed.
            print (now + " -> Renamed: " + event.src_path)

if __name__ == '__main__':
    w = Watcher()
    w.run()
