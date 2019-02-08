import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY = "C:\Projetos"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("There was an error trying to get an eagle view.")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("Created: " + event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Modified: " + event.src_path)
        
        elif event.event_type == 'deleted':
            # Taken any action here when a file is deleted.
            print ("Deleted: " + event.src_path)
       
        elif event.event_type == 'moved':
            # Taken any action here when a file is renamed.
            print ("Renamed directory: " + event.src_path)

if __name__ == '__main__':
    w = Watcher()
    w.run()