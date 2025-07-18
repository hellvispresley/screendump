import os
import shutil
import time
import datetime
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import FileSystemEventHandler

# ✅ SET THESE TO MATCH YOUR SYSTEM
SRC_FOLDER = "/mnt/c/Users/<Change to Your User/Pictures/Screenshots"
DEST_FOLDER = "/home/<Change To Your User/projects/screendump/screenshots"

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            ext = os.path.splitext(event.src_path)[1].lower()
            clean_name = f"screenshot_{timestamp}{ext}"
            dest_path = os.path.join(DEST_FOLDER, clean_name)

            try:
                shutil.copy2(event.src_path, dest_path)
                print(f"Copied and renamed: {clean_name}")
            except Exception as e:
                print(f"Error copying {clean_name}: {e}")

if __name__ == "__main__":
    os.makedirs(DEST_FOLDER, exist_ok=True)
    print(f"Watching for new screenshots in: {SRC_FOLDER}")
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, path=SRC_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
