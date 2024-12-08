"""
Features:
1. Type in a txt file and have code watching it (running continuously). 
2. A specific exit indicator code should save the file and auto-open a new one.
3. A specific kill indicator code should stop the continuous monitoring.
3. Files should be saved into a logical folder structure with a specified name, taken from the first line of each file.
   Ex: jacob/klonsky/myfile.txt would save myfile.txt in folder klonsky within folder jacob (sitting at same level as the code)
   Part of this use is so that it is easily uploadable to google drive.
4. Additional feature: File Combining - specify the highest level folder and it will combine all the files, segmenting them by
   folder with headers.
   - This feature likely requires a separate txt file that is aware of the folder schema 

"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"{event.src_path} was modified")

    def on_created(self, event):
        print(f"{event.src_path} was created")

def main():
    path = "."  # Path to monitor
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True) # Does this require event_handler? 
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()