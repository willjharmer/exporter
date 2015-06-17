"""
Monitors our code & docs for changes
"""
import os
import sys
import subprocess
import datetime
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def get_now():
    "Get the current date and time as a string"
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def run_feature_tests():
    "Run lettuce features"

    print >> sys.stderr, "Running lettuce at %s" % get_now()
    os.chdir(BASEDIR)
    subprocess.call(r'lettuce')

def getext(filename):
    "Get the file extension."

    return os.path.splitext(filename)[-1].lower()

class ChangeHandler(FileSystemEventHandler):
    """
    React to changes in Python, nosetest and lettuce files by
    running nosetests and lettuce
    """

    def on_any_event(self, event):
        "If any file or folder is changed"

        if event.is_directory:
            return
        if getext(event.src_path) == '.py':
            run_feature_tests()

def main():
    """
    Called when run as main.
    Look for changes to code files.
    """

    while 1:

        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, BASEDIR, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == '__main__':
    main()
