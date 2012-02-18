import dropbox
import time

class Storage:
    def __init__(self):
        self.name = ""

    def start(self):
        pass

    def stop(self):
        pass

class PendriveStorage(Storage):
    pass

class DropboxStorage:
    def __init__(self):
        self.name = "origin"

    def start(self):
        dropbox.start([])
        self.wait_for_dropbox_sync()

    def stop(self):
        self.wait_for_dropbox_sync()
        dropbox.stop([])

    def wait_for_dropbox_sync(self):
        print("Waiting for dropbox sync")
        time.sleep(5)
        while dropbox.status([]) != "Idle":
            time.sleep(1)
